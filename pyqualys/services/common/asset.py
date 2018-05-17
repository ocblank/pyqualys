# -*- coding: utf-8 -*-
import logging
from .scan import scanner, ScanAsset

logger = logging.getLogger(__name__)


class AssetHandler(object):

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.asset_api_version = api_version
        self.asset_urls_map = urls_map.asset
        self.urls_map = urls_map
        super(AssetHandler, self).__init__(session=session,
                                           api_version=api_version,
                                           urls_map=urls_map)

    @scanner
    def get_obj(self, **data):
        uri = self.asset_api_version + self.asset_urls_map
        resp = self.session.post(uri, data)
        logger.debug(resp.text)
        return {'response': resp, "info": {"endpoint": self.asset_api_version,
                                           "uri": self.urls_map,
                                           "session": self.session}}

    def add_asset(self, **kwargs):
        if "title" not in kwargs and "ips" not in kwargs:
            logger.error("title or ips is missing.")
        data = kwargs
        data["action"] = "add"

        return self.get_obj(**data)

    def update_asset(self, **kwargs):
        logger.debug("Updating Asset: {}".format(kwargs))
        if "asset_id" not in kwargs and "ids" not in kwargs:
            logger.error("asset_id or ids is missing.")
            return
        if "asset_id" in kwargs:
            asset_id = kwargs.pop("asset_id")

        data = {}
        for key in kwargs.copy():
            if not key.startswith("set_"):
                data["set_"+key] = kwargs.pop(key)
            else:
                data[key] = kwargs.pop(key)

        data["id"] = asset_id
        data["action"] = "edit"

        return self.get_obj(**data)

    def delete_asset(self, asset_id):
        logger.debug("Deleting Asset: {}".format(asset_id))
        data = {"action": "delete", "id": asset_id}

        return self.get_obj(**data)

    def list_assets(self):
        logger.debug("List of the Asset")
        data = {"action": "list", "show_attributes": "ALL"}

        return self.get_obj(**data)

    def search_asset(self, **kwargs):
        logger.debug("Search the asset: {}".format(kwargs))
        if "asset_id" not in kwargs and "ids" not in kwargs:
            logger.error("asset_id or ids is missing.")
            return
        if "asset_id" in kwargs:
            kwargs["ids"] = kwargs.pop("asset_id")
        data = kwargs
        data["action"] = "list"

        return self.get_obj(**data)
