import pandas as pd
import os 
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'users.xlsx')
if not os.path.exists(file_path):
    print("xlsx文件不存在，请检查路径")
else:
    df = pd.read_excel(file_path)
    output_dir = os.path.join(current_dir, 'userdata')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for index, row in df.iterrows():
        uuid = row['player_uuid']
        balance = row['Balance']
        file_name = os.path.join(output_dir, f"{uuid}.yml")
        with open(file_name, 'w') as file:
            file.write(f"money: '{balance}'")
    print("数据已创建完成")