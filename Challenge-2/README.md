# challenge-2
Tested on Python version: 3.6.8
Libraries to be downloaded:
 - json
 - sys
 - glom
 - requests

The script expects one argument in the form of a string, which is the metadata key for which user wishes to find the respective value

For example:
 python3 get_metadata.py ami-id

 Output:
 Target key found
 ami-id : ami-0c056961c241069cb

In case of faulty key:
 python3 get_metadata.py ami-idhda

 Output:
 Incorrect key

Please ensure to pass only the final key to the script and not the entire nested path
For "curl http://169.254.169.254/latest/meta-data/iam/info"
CORRECT: python3 get_metadata.py info
INCORRECT: python3 get_metadata.py iam/info

### The script also creates a JSON file instance_metadata.json in the workspace which will contain the the entire metadata of the instance

