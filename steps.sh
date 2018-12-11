# @Author: ahmedkammorah
# @Date:   2018-06-04 14:47:54
# @Last Modified by:   ahmedkammorah
# @Last Modified time: 2018-06-04 14:50:27


# To create Flask app with JWT 
# clone me

# it debent on local dir on 
/ak 

# Edit project name
# Build container
sh build_dev_image.sh

# edit container name or number 
# run container
sh run_ak_dev.sh
# inside container
python MainApp/AKAppMain.py  

# Or 
sh run_ak_pro.sh