# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import mail_folder_request_builder # import MailFolderRequestBuilder
#from .mail_folder_request_builder import MailFolderRequestBuilder
from ..model.mail_folder import MailFolder
import json

class MailFolderCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the MailFolderCollectionRequest
        
        Args:
            request_url (str): The url to perform the MailFolderCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(MailFolderCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the MailFolderCollectionPage

        Returns: 
            :class:`MailFolderCollectionPage<microsoft.msgraph.request.mail_folder_collection.MailFolderCollectionPage>`:
                The MailFolderCollectionPage
        """
        self.method = "GET"
        collection_response = MailFolderCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class MailFolderCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the MailFolderRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a MailFolderRequestBuilder for
        
        Returns: 
            :class:`MailFolderRequestBuilder<microsoft.msgraph.request.mail_folder_request_builder.MailFolderRequestBuilder>`:
                A MailFolderRequestBuilder for that key
        """
        return mail_folder_request_builder.MailFolderRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the MailFolderCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`MailFolderCollectionRequest<microsoft.msgraph.request.mail_folder_collection.MailFolderCollectionRequest>`:
                The MailFolderCollectionRequest
        """
        req = MailFolderCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the MailFolderCollectionPage

        Returns: 
            :class:`MailFolderCollectionPage<microsoft.msgraph.request.mail_folder_collection.MailFolderCollectionPage>`:
                The MailFolderCollectionPage
        """
        return self.request().get()



class MailFolderCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`MailFolderCollectionPage<microsoft.msgraph.request.mail_folder_collection.MailFolderCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = MailFolderCollectionPage(self._prop_dict["value"])

        return self._collection_page


class MailFolderCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the MailFolder at the index specified
        
        Args:
            index (int): The index of the item to get from the MailFolderCollectionPage

        Returns:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The MailFolder at the index
        """
        return MailFolder(self._prop_list[index])

    def mail_folder(self):
        """Get a generator of MailFolder within the MailFolderCollectionPage
        
        Yields:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The next MailFolder in the collection
        """
        for item in self._prop_list:
            yield MailFolder(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the MailFolderCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = MailFolderCollectionRequest(next_page_link, client, options)
