# Setting up Data Lake using ADLS

## Getting Started with ADLS

Azure data lake is also a cloud based storage service which supports big data analytics. You can store structured, non structured or semi structured data into it.

Let us get started with ADLS or Azure Data Lake Storage

* Highly secure with flexible mechanisms.
* Cost optimisation
* Limitless scale 
* You can review details about ADLS followig [documentation](https://azure.microsoft.com/en-in/products/storage/data-lake-storage/#overview)

## Overview of ADLS Web UI

Let us get an overview of ADLS Web UI

We can use ADLS Web UI to get started with Azure Cloud Storage Quickly.

Following are the common tasks using Azure Web UI

* Upload Files and Folders from Local File System to ADLS
* To manage containers 
* Delete files and folders from ADLS
* Review the details of files and folders

Even though it is easy to start with ADLS Web UI, it is not good idea to use in projects. We typically use Commands or Programming Language SDKs.

## Setup ADLS Container and Upload File

As part of this lecture, we will setup ADLS Container and upload files from local file system to ADLS Container.

* Container Name - **itvcontainer**
* Upload retail_db folder to ADLS using Web UI.

## Overview of `az`

`az` command is used to manage containers, folders and files in ADLS

* `az help` can be used to get help.
* Here are the most important commands to manage containers, folders and files using `az`.
* We have used Cloud Shell to run `az` commands for the demo. Here are the commands we have used for the demo related to get started with `az`.

```
az -h #to get usage or help on ls or list command
az account  #Manage Azure subscription information

```

## Setup Data Repository in Azure Cloud Shell

Here are the details to setup data repository in Azure Cloud Shell.

* Clone our data repository from GitHub.
* You can use following command to clone the repository.

`git clone https://github.com/dgadiraju/data`
* You can review the retail files in the data folder by running `find data/retail_db`
* You can also use `ls -ltr` data to list all the data sets that are available in our GitHub repository.

## Overview of Data Sets
Let us get a quick overview about data sets

* Data Sets are part of our GitHub repository.
* If you have already setup GitHub repository, you should see `data` folder.
* We will use these data sets as part of different sections or modules in this course.

## Manage Files in ADLS using az commands

Let me demonstrate how to manage files in `itvcontainer` container.

* Delete the container, if it exists (we need to empty the folder first).
* Create the container.
* Add `data/retail_db` recursively to your cotainer recursively.
* Review all the files in `data/retail_db` and container.
* Make sure all the files are successfully copied.
* Here are some of the important commands we can use to manage containers, folders as well as files.

|Command|Description|
|---|---|
|`az storage fs create -n container-name --account-name storage-account-name`|To create container|
|`az storage fs delete -n container-name --account-name storage-account-name`|To remove container|
|`az storage fs file list -f container-name --account-name storage-account-name`|To list files and folders in container|
|`az storage fs directory upload -f container-name --account-name storage-account-name -s "data\retail_db" --recursive`|To copy retail_db folder recursively from local file system to container in specified path|


## Manage Files in ADLS using Python

Let us see how we can manage files in ADLS using Python as Programming Language.

* We need to first make sure some Azure packages are installed.
* Install azure-storage-blob Python library using pip.
* Initialize a client instance with a storage connection string

Refer to the Notebook which have few examples related to managing files in ADLS using Python





