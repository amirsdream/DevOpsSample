import sys
import os
from shutil import copyfile
import string
import re

MICROSERVICEFILES=["service.yaml","deployment.yaml","ingress.yaml","configmap.yaml","job.yaml","mysql-value.yaml","persistentVolumeClaim.yaml","persistentVolume.yaml","collectstaticjob.yaml","loaddatajob.yaml","migratejob.yaml","my.cnf","persistentVolumestaticdata.yaml","persistentVolumeClaimstaticdata.yaml"]

def main():
    input1 = sys.argv[1]
    directory= "/root/microservice/"+input1+"/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for f in MICROSERVICEFILES:
        copyfile(f, directory+f)
        with open(directory+f) as file:
            file_str = file.read()
        file_str = file_str.replace( "relation" , input1)
        file_str = file_str.replace( "django-k8s-starter-config" , "django-"+input1+"-config")
        file_str = file_str.replace( "appdir" , sys.argv[2])
        if "ingress.yaml" == f:
            a = sys.argv[1].replace( "-" , "/" )
            b = ""
            try:
                b = re.findall(r'\bsecim.*?$', a)[0]
                b = b.replace("/","_")
                a = re.sub(r'\bsecim.*?$',b, a)
            except:
                pass
            a = a.replace("/v1", " ")
            print(a)
            file_str= file_str.replace( "- path: /" , "- path: /"+a)
        file.close()
        with open(directory+f, "w") as file:
            file.write(file_str)
      #  print(file_str)
    os.chdir(directory)
#    print(os.getcwd())



if __name__ == "__main__":
   main()
