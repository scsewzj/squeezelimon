import requests
import pandas as pd
import argparse
import os
import importlib.resources



print("🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋")
print("Welcome to the 🍋🍋🍋Squeezelimon🍋🍋🍋 Lipid Topology File Downloader!")
print("This tool is derived from the Limonada database and allows you to query and download lipid topology files based on various criteria.")
print("It is for educational and research purposes only. Please ensure you have the necessary permissions to download and use the files.")
print("Author: Zhouji WU, University Paris-Saclay, France")
print("Version: 1.0 (2024-04-16)")
print("The author is not responsible for any misuse of this tool or the downloaded files. Always respect intellectual property rights and use the files in accordance with their licenses.")

print("🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋")
print("We Sincerely thank the Limonada team at University of Reims Champagne-Ardenne for maintaining this valuable resource.")
print("For more information, please refer to: https://limonada.univ-reims.fr/")
print("🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋")

def load_data(metatable_path, links_path):
    df_all = pd.read_csv(metatable_path)
    with open(links_path, 'r') as f:
        all_links = [line.strip() for line in f]
    return df_all, all_links

def query_link(links, filename, ff=None, lipid=None, project=None, software=None):
    conds = [filename, ff, lipid, project, software]
    conds = [str(cond).lower() for cond in conds if cond is not None]
    subs = []
    for link in links:
        lower_link = link.lower()
        if all(cond in lower_link for cond in conds):
            subs.append(link)
    return subs

def selectdownload(subs):
    root = "https://limonada.univ-reims.fr"
    if len(subs) == 0:
        print("🍋No matching links found.")
    elif len(subs) == 1:
        print(f"🍋Perfect match found: {subs[0]}")
        print("🍋Downloading...")
        downloadlink = root + subs[0]
        response = requests.get(downloadlink, timeout=30)
        filename = subs[0].split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"🍋Downloaded: {filename}")
    else:
        print("🍋Multiple matches found:")
        for i, sub in enumerate(subs):
            print(f"{i + 1}: {sub}")
        choice = int(input("🍋Enter the number of the link to download: "))
        if 1 <= choice <= len(subs):
            selected_link = subs[choice - 1]
            print(f"🍋Selected: {selected_link}")
            print("🍋Downloading...")
            downloadlink = root + selected_link
            response = requests.get(downloadlink, timeout=30)
            filename = selected_link.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"🍋Downloaded: {filename}")
        else:
            print("🍋Invalid choice. No download performed.")

def main():
    argparser = argparse.ArgumentParser(description='🍋Query and download lipid topology files.')
    argparser.add_argument('--filename', type=str, required=True, help='🍋Name of the topology file (e.g., POPC.itp)')
    argparser.add_argument('--ff', type=str, help='🍋Force field (e.g., charmm36)')
    argparser.add_argument('--lipid', type=str, help='🍋Lipid name (e.g., POPC)')
    argparser.add_argument('--project', type=str, help='🍋Project name(e.g., klauda2010)')
    argparser.add_argument('--software', type=str, help='🍋Software (e.g., gromacs)')
    args = argparser.parse_args()
    
    csv_path = importlib.resources.files("squeezelimon") / "lipid_top_db.csv"
    txt_path = importlib.resources.files("squeezelimon") / "lipid_top_links.txt"
    df_all, all_links = load_data(str(csv_path), str(txt_path))
    qed_links = query_link(all_links, filename=args.filename, ff=args.ff, lipid=args.lipid, project=args.project, software=args.software)
    selectdownload(qed_links)
            
if __name__ == "__main__":
    main()