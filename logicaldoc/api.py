# -*- coding: utf-8 -*-
# © 2016 Francesco Apruzzese <cescoap@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

API_REST = {
    '7.5.1': {
        'DocumentDelete': {
            'type': 'delete',
            'url': '{LD_url}/services/rest/document/delete',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'DocumentGetContent': {
            'type': 'get',
            'url': '{LD_url}/services/rest/document/getContent',
            'headers': {'Content-Type': 'application/octet-stream'}
            },
        'DocumentGetDocument': {
            'type': 'get',
            'url': '{LD_url}/services/rest/document/getDocument',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'DocumentList': {
            'type': 'get',
            'url': '{LD_url}/services/rest/document/list',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'DocumentListDocuments': {
            'type': 'get',
            'url': '{LD_url}/services/rest/document/listDocuments',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'DocumentUpdate': {
            'type': 'put',
            'url': '{LD_url}/services/rest/document/update',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'FolderRename': {
            'type': 'put',
            'url': '{LD_url}/services/rest/folder/rename',
            'headers': {'Content-Type': 'application/json'}
            },
        'FolderUpdate': {
            'type': 'post',
            'url': '{LD_url}/services/rest/folder/update',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        'SearchFind': {
            'type': 'post',
            'url': '{LD_url}/services/rest/search/find',
            'headers': {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
            },
        },
    }
