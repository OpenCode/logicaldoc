# -*- coding: utf-8 -*-
# © 2016 Francesco Apruzzese <cescoap@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# Documentation:
# * http://wiki.logicaldoc.com/rest/

import requests
from .api import API_REST


class LogicalDoc(object):

    def __init__(self, url='http://localhost:8080', user='admin',
                 password='admin', version='7.5.1'):
        self._url = url
        self._user = user
        self._password = password
        self._version = version
        self.language = 'en'

    def __str__(self):
        return 'LogicalDoc on {url} with {user}'.format(
            url=self._url, user=self._user)

    @property
    def auth(self):
        return self._user, self._password

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    def execute(self, service='', data=None):
        """
        Generic execute called from all api methods
        :param service: Service to invoke
        :param data: Dict with informations for called service
        :return: Response of the request
        """
        if service:
            # ----- Get right url based on API_REST version
            #       Invoke the right requst type based on method call type
            if API_REST.get(self._version, False):
                url = API_REST[self._version][service]['url']
                url = url.format(LD_url=self._url)
                request = False
                # ----- Get
                if API_REST[self._version][service]['type'] == 'get':
                    request = requests.get(
                        url, auth=self.auth, params=data,
                        headers=API_REST[self._version][service]['headers'])
                # ----- Post
                elif API_REST[self._version][service]['type'] == 'post':
                    request = requests.post(
                        url, auth=self.auth, json=data,
                        headers=API_REST[self._version][service]['headers'])
                # ----- Put
                elif API_REST[self._version][service]['type'] == 'put':
                    request = requests.put(
                        url, auth=self.auth, json=data,
                        headers=API_REST[self._version][service]['headers'])
                # ----- Delete
                elif API_REST[self._version][service]['type'] == 'delete':
                    request = requests.delete(
                        url, auth=self.auth, json=data,
                        headers=API_REST[self._version][service]['headers'])
                return request
        else:
            return False

    @staticmethod
    def _check_data_keys(keys, data):
        if not (keys and data):
            return False
        data_keys = data.keys()
        for key in keys:
            if key not in data_keys:
                return False
        return True

    # -------------
    # DOCUMENT APIs
    # -------------

    def document_checkin(self, data):
        """
        Performs a check-in (commit) operation of new content 
        over an existing document. 
        The document must be in checked-out status
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def document_checkout(self, data):
        """
        Performs the checkout operation on a document. 
        The document status will be changed to checked-out
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def document_create(self, data):
        """
        Creates a new document using the metadata 'document' 
        object provided as JSON/XML
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def document_delete(self, data):
        """
        Delete a document
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def document_get_content(self, data):
        """
        Returns the content of a document using the document ID in input
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('DocumentGetContent', data)

    def document_get_document(self, data):
        """
        Gets the document metadata
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('DocumentGetDocument', data)

    def document_list(self, data):
        """
        Lists Documents by folder identifier
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('DocumentList', data)

    def document_list_documents(self, data):
        """
        Lists Documents by folder ID filtering the results by filename
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('DocumentListDocuments', data)

    def document_update(self, data):
        """
        Updates the metadata of an existing document
        :param data: Dict with informations
        :return: Response of the request
        """
        # -----  Check data
        if not self._check_data_keys(('id', 'folderId', 'fileName'), data):
            raise UserWarning(
                '"id", "folderId" and "fileName" must be defined')
        return self.execute('DocumentUpdate', data)

    def document_upload(self, data):
        """
        Creates or updates an existing document
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    # -----------
    # FOLDER APIs
    # -----------

    def folder_create(self, data):
        """
        Creates a new folder
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_create_folder(self, data):
        """
        Creates a new subfolder
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_create_path(self, data):
        """
        Creates a path of folders starting from a parent folder
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_create_simple(self, data):
        """
        Creates folders using an input path. 
        All the folders in the path will be created
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_create_simple_form(self, data):
        """
        Creates folders using an input path
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_create_simple_json(self, data):
        """
        Creates folders using an input path. 
        All the folders in the path will be created
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_delete(self, data):
        """
        Delete a folder
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_get_folder(self, data):
        """
        Gets the folder with the specified ID
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_get_path(self, data):
        """
        Returns the folders that make up the path to the folder in input
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_get_path_string(self, data):
        """
        Returns the path to the folder in input
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_list_children(self, data):
        """
        Returns the list of child folders
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_move(self, data):
        """
        Updates a folder by changing its parent. 
        The folder is moved to the new parent folder
        :param data: Dict with informations
        :return: Response of the request
        """
        raise NotImplementedError('Not implemented, yet')

    def folder_rename(self, data):
        """
        Changes the name of a given folder
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('FolderRename', data)

    def folder_update(self, data):
        """
        Updates a folder changing its metadata
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('FolderUpdate', data)

    # -----------
    # SEARCH APIs
    # -----------

    def search_find(self, data):
        """
        Runs a search on the server
        :param data: Dict with informations
        :return: Response of the request
        """
        return self.execute('SearchFind', data)
