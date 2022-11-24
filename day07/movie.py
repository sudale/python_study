import pandas as pd

# xlsx -> csv 파일변환

em_df = pd.ExcelFile('KOBIS_boxoffice.xlsx').parse(
    sheet_name=0, dtype=object, engine='xlrd', verbose=True)


# csv로 파일 변환
em_df.to_csv(path_or_buf='KOBIS_boxoffice.csv', sep=',',
             header=True, index=False, mode='w', encoding='CP949')

# em_df에 해당 csv파일 삽입
em_df = pd.read_csv('KOBIS_boxoffice.csv', engine='c',
                    dtype=str, sep=',', encoding='CP949')
