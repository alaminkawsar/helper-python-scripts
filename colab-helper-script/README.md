# How to Download Another person's shared google drive folder!

```
!pip install gdown

#collapse-output
import gdown
url = "https://drive.google.com/drive/folders/1Kx69IybABCG5mOmZIiii--fqjpVgYx2h"
gdown.download_folder(url, quiet=True, use_cookies=False)
```

Here: <br>
```url``` is shared folder url. See to top search bar of your browser when you open the folder. <br>
The folder will be saved as ```content/SHARED_FOLDER/```