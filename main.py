# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:49:58 2021

@author: Jeffrey

We want to create an API to allow other system to communicate with the data server. 
In this case, the data is static and is store in a csv file.
No need to get POST and UPDATE requests.

Simple coding standard:
i = integer
s = string

"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from collections import OrderedDict
from operator import getitem
import csv

app = Flask(__name__)
api = Api(app)

dict_shows = {}


def Sort_Top10_Shows(the_dict_shows):
    # Sort nested dictionary by key
    dict_result = OrderedDict(sorted(the_dict_shows.items(), key = lambda x: getitem(x[1], 'Title')))
    return dict_result


# To make sure that the GET request is valid
def Abort_If_Provider_Not_Valid(the_dict_shows):
    if len(the_dict_shows) == 0:
        abort("Provider name is not valid, please enter a valid one...")


# To make sure that the GET request by page is valid
def Abort_If_Page_Number_Not_Valid():
    abort("Page number is not valid, please enter a valid one...")


# Get the data from csv file and add to dictionary. No need to loop through all the csv, just the top shows required.
def Read_From_Csv(sProvider):
    with open('assets.csv', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        iIndex = 0
        for line in csv_reader:
            if iIndex <= 10:
                if iIndex == 0:
                    iIndex = iIndex+1
                    continue
                sShowId = str(line[0])
                sProviderName = str(line[1])
                sTitle = str(line[2])
                iNumberOfViews = line[3]

                if sProviderName == sProvider:
                    dict_shows[sShowId] = {"Provider": sProviderName, "Title": sTitle, "Views": iNumberOfViews}
                    iIndex = iIndex+1


# To handle pagination of the data
def Pagination(the_dict_shows, iPage):
    # Sort the top 10 shows by title first
    dict_sorted_shows = Sort_Top10_Shows(the_dict_shows)
    dict_result = {}
    iShowsPerPage = 4
    iPageNumber = 1
    iIndex = 1

    for key in dict_sorted_shows:
        dict_to_add = {"Id": str(key)}
        dict_to_add.update(dict_sorted_shows[key])
        if iIndex == 1:
            dict_result[iPageNumber] = [dict_to_add]
        else:
            dict_result[iPageNumber].append(dict_to_add)

        if iIndex == iShowsPerPage:    
            iPageNumber = iPageNumber+1
            iIndex = 0
        iIndex = iIndex+1

    if iPage in dict_result:
        return dict_result[iPage]
    else:
        Abort_If_Page_Number_Not_Valid()


# Get request to return the top 10 shows using API that supports pagination
class TopShowsInPages(Resource):
    def get(self, sProvider, iPage):

        # We clear at the beginning of every GET request to prevent it from stacking on every GET request.
        dict_shows.clear()
        Read_From_Csv(sProvider)
        dict_result = Pagination(dict_shows, iPage)

        return dict_result


# Get request to return all the top 10 show without pagination
class GetAllTopShowsInOnePage(Resource):
    def get(self, sProvider):

        dict_shows.clear()
        Read_From_Csv(sProvider)
        Abort_If_Provider_Not_Valid(dict_shows)
        dict_result = Sort_Top10_Shows(dict_shows)

        return dict_result


# App routes links
api.add_resource(TopShowsInPages, "/shows/<string:sProvider>/<int:iPage>")
api.add_resource(GetAllTopShowsInOnePage, "/shows/<string:sProvider>")


if __name__ == "__main__":
    app.run(debug=True)