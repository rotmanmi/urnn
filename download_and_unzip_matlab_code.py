import os
import urllib.request 
import zipfile as zipfile2
import gzip
import requests


packages=[ \
          {'url': 'http://ecs.utdallas.edu/loizou/speech/composite.zip', 'local': 'composite.zip', 'dir': 'evaluation/obj_evaluation'},
          {'url': 'http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/voicebox.zip', 'local': 'voicebox.zip', 'dir': 'evaluation/voicebox'},
          {'url': 'http://ceestaal.nl/stoi.zip', 'local': 'stoi.zip', 'dir': 'evaluation/stoi'},
          {'url': 'https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/19550/versions/1/download/zip', 'local': 'rdir.zip', 'dir': 'rdir'} \
         ]

for package in packages:
    src=package['url']
    dest=package['local']
    path=package['dir']
    print ("Downloading file %s to %s" % (src,dest))
    r = requests.get(src)
    with open(dest, 'wb') as outfile:
        outfile.write(r.content)    

    # opener.retrieve(src,dest)
    print ("Unzipping file %s..." % (dest))

    outpath='matlab/' + package['dir']
    if not os.path.exists(outpath):
        print ("Creating directory %s" % outpath)
        os.makedirs(outpath)

    try:
        with zipfile2.ZipFile(dest, 'r') as f:
            f.extractall(outpath)
    except:
        print ("Failed to extract file %s to %s" % (dest, outpath))
