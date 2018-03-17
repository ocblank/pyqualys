
class UserHandler:

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.user_api_version = "api/1.0/" # api_version
        self.user_urls_map = urls_map.user
        self.acceptEULA = False
        super(UserHandler, self).__init__()

    # @property
    # def verifyEULA(self):
    #     return self.acceptEULA

    # @verifyEULA.setter
    # def verifyEULA(self, user):
    #     print(user)

    def add_user(self, **parameter):
        """
        Create new user and became part of a given service.

        :param parameter: contain the user information.
        :type parameter: dict

        :format
        {
            'first_name': 'fname',
            'last_name': 'lname',
            'title': 'My Title',
            'phone': 012345689,
            'fax': 022,
            'email': 'fname@company.com',
            'address1': 'Panchshil Tech Park',
            'address2': 'Shivaji Nagar',
            'city': 'Pune',
            'country': 'India',
            'state': 'Maharashtra',
            'zip_code': 411022,
            'external_id': 101,

            'send_email': 0,

            'user_role': 'role',
            'business_unit': 'bu',
            'asset_group': 'grp1, grp2',
            'ui_interface_style': 'red',


            'time_zone_code': 2
        }
        """
        parameter["action"] = "add"
        uri = self.user_api_version + self.user_urls_map
        resp = self.session.post(uri, parameter)
        return resp

    def edit_user(self, **parameter):
        """
        Update the user details.

        :param parameter: contain the updated user filed.
        :type parameter: dict
        """


    def delete_user(self, username, force=True):
        """
        Delete the user from records.

        :param username: username of user.
        :type username: string

        :param force: clean all user informations.
        :type force: bool
        """

    def get_users(self):
        """
        Return list of users.
        """

    def search_user(self, query):
        """
        Find the user by the help of given query.

        :param query: multiple search terms in one string.
                    username=qualys* AND ip=10.*
        :param query: string
        """
        pass
