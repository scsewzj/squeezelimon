# Squeezelimon: Lipid Topology File Downloader
```
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
Welcome to the 🍋🍋🍋Squeezelimon🍋🍋🍋 Lipid Topology File Downloader!
This tool is derived from the Limonada database and allows you to query and download lipid topology files based on various criteria.
It is for educational and research purposes only. Please ensure you have the necessary permissions to download and use the files.
Author: Zhouji WU, University Paris-Saclay, France
Version: 1.0 (2024-04-16)
The author is not responsible for any misuse of this tool or the downloaded files. Always respect intellectual property rights and use the files in accordance with their licenses.
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
We Sincerely thank the Limonada team at University of Reims Champagne-Ardenne for maintaining this valuable resource.
For more information, please refer to: https://limonada.univ-reims.fr/
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
```

## Installation
```
pip install SqueezeLimon
```

## Usage Example
### Shell
```
MacBook-Pro% squeezelimon --filename popc.itp
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
Welcome to the 🍋🍋🍋Squeezelimon🍋🍋🍋 Lipid Topology File Downloader!
This tool is derived from the Limonada database and allows you to query and download lipid topology files based on various criteria.
It is for educational and research purposes only. Please ensure you have the necessary permissions to download and use the files.
Author: Zhouji WU, University Paris-Saclay, France
Version: 1.0 (2024-04-16)
The author is not responsible for any misuse of this tool or the downloaded files. Always respect intellectual property rights and use the files in accordance with their licenses.
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
We Sincerely thank the Limonada team at University of Reims Champagne-Ardenne for maintaining this valuable resource.
For more information, please refer to: https://limonada.univ-reims.fr/
🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
🍋Multiple matches found:
1: /media/topologies/Gromacs/Charmm27/POPC/Feller2000/POPC.itp
2: /media/topologies/Gromacs/charmm36/POPC/Klauda2010/POPC.itp
3: /media/topologies/Gromacs/martini_2.0/POPC/Wassenaar2015/POPC.itp
4: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014_Z/POPC.itp
5: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014/POPC.itp
6: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2017_Z/POPC.itp
7: /media/topologies/Gromacs/opls-aa_Rog2016/POPC/Kulig2015/POPC.itp
8: /media/topologies/Gromacs/slipids/POPC/Jambeck2012/POPC.itp
🍋Enter the number of the link to download: 
```

### Python
```
In [1]: from squeezelimon import squeeze
In [2]: df_all, all_links = squeeze.load_data()

In [3]: subs = squeeze.query_link(all_links, filename='popc.itp')

In [4]: subs
Out[4]: 
['/media/topologies/Gromacs/Charmm27/POPC/Feller2000/POPC.itp',
 '/media/topologies/Gromacs/charmm36/POPC/Klauda2010/POPC.itp',
 '/media/topologies/Gromacs/martini_2.0/POPC/Wassenaar2015/POPC.itp',
 '/media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014_Z/POPC.itp',
 '/media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014/POPC.itp',
 '/media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2017_Z/POPC.itp',
 '/media/topologies/Gromacs/opls-aa_Rog2016/POPC/Kulig2015/POPC.itp',
 '/media/topologies/Gromacs/slipids/POPC/Jambeck2012/POPC.itp']

In [5]: squeeze.selectdownload(subs)
🍋Multiple matches found:
1: /media/topologies/Gromacs/Charmm27/POPC/Feller2000/POPC.itp
2: /media/topologies/Gromacs/charmm36/POPC/Klauda2010/POPC.itp
3: /media/topologies/Gromacs/martini_2.0/POPC/Wassenaar2015/POPC.itp
4: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014_Z/POPC.itp
5: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2014/POPC.itp
6: /media/topologies/Gromacs/martini_2.0/POPC/Ingolfsson2017_Z/POPC.itp
7: /media/topologies/Gromacs/opls-aa_Rog2016/POPC/Kulig2015/POPC.itp
8: /media/topologies/Gromacs/slipids/POPC/Jambeck2012/POPC.itp
🍋Enter the number of the link to download: 2
🍋Selected: /media/topologies/Gromacs/charmm36/POPC/Klauda2010/POPC.itp
🍋Downloading...
🍋Downloaded: POPC.itp
```