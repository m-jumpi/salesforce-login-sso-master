# Description #
Easy to use python library to perform SSO login to Salesforce. Can be used in any python project. Since login with Salesforce credentials is disabled, SSO is the only way to login to Salesforce.
Current version supports 2 logon methods:
*  Kerberos login. When started using amust account, no credentials are required. Easiest and recommended method
*  Form based login. Amust credentials are required


### Requirements ###
* Python 3 

# Setup #
Lib can be used in single python project or can be shared between multiple. We'll cover both approaches.
Examples are made primarily for Windows, linux setup can slightly differ.

This document assumes python 3.7.4 is used. It's safe to use later versions as well.


### Installing prerequisites on Windows ###
1.  Install python 3 [from here](https://www.python.org/downloads/release/python-374/). Check add python to path variable
2.  Install [git scm](https://git-scm.com/download/win)
3.  Start git bash
4.  Upgrade pip: `python -m pip install --upgrade pip`
5.  Install virtualenv: `pip install virtualenv`


### Setup for single project ###
Create a new folder for your project. Assume it's c:\python\sf_proj

1. Open git bash and run `cd /c/python/sf_proj/`
2. Clone project:  `git -c http.sslVerify=false clone https://git.support2.veeam.local/vkuznetsov/salesforce-login-sso.git .`
3. Create virtual environment in venv folder: `virtualenv venv`
4. Activate virtual environment `source venv/Scripts/activate`
5. Install requirements: `pip install -r requirements.txt` Make sure commands runs successfully
6. Run example.py: `python example.py` Verify it runs successfully
7. Implement lib usage in your project similar to example.py

### Setup for multiple projects ###
1. Create folder where python libs will be located. For example c:\python
2. Add that folder to PYTHONPATH environment variable
3. Download salesforce_sso folder from https://git.support2.veeam.local/vkuznetsov/salesforce-login-sso to c:\python

Initialize project to use lib:
1. Create project folder, virtual environment and activate it
2. Download requirements.txt from repository and install it
3. Download example.py from repository to project folder and run it with python. Verify it runs fine