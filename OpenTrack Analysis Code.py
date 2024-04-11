import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import os

def analyze_and_save(file_path, save_directory, stats_raw_combined, stats_filtered_combined):
    # CSV 파일 로드
    df = pd.read_csv(file_path)

    # 샘플링 레이트를 사용하여 샘플링된 시간을 계산합니다.
    sampling_rate = 250  # Hz
    df['scaled_time'] = df.index / sampling_rate

    # 원시 데이터와 필터링된 데이터의 통계 계산
    stats_raw = df[['rawYaw', 'rawPitch', 'rawRoll']].agg(['mean', 'std', 'min', 'max'])
    stats_filtered = df[['filteredYaw', 'filteredPitch', 'filteredRoll']].agg(['mean', 'std', 'min', 'max'])

    # 파일명 추출 (확장자 없이)
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # 통계값을 combined 데이터프레임에 추가
    stats_raw_combined.loc[file_name, 'mean_rawYaw'] = stats_raw.loc['mean', 'rawYaw']
    stats_raw_combined.loc[file_name, 'mean_rawPitch'] = stats_raw.loc['mean', 'rawPitch']
    stats_raw_combined.loc[file_name, 'mean_rawRoll'] = stats_raw.loc['mean', 'rawRoll']
    stats_raw_combined.loc[file_name, 'std_rawYaw'] = stats_raw.loc['std', 'rawYaw']
    stats_raw_combined.loc[file_name, 'std_rawPitch'] = stats_raw.loc['std', 'rawPitch']
    stats_raw_combined.loc[file_name, 'std_rawRoll'] = stats_raw.loc['std', 'rawRoll']
    stats_raw_combined.loc[file_name, 'min_rawYaw'] = stats_raw.loc['min', 'rawYaw']
    stats_raw_combined.loc[file_name, 'min_rawPitch'] = stats_raw.loc['min', 'rawPitch']
    stats_raw_combined.loc[file_name, 'min_rawRoll'] = stats_raw.loc['min', 'rawRoll']
    stats_raw_combined.loc[file_name, 'max_rawYaw'] = stats_raw.loc['max', 'rawYaw']
    stats_raw_combined.loc[file_name, 'max_rawPitch'] = stats_raw.loc['max', 'rawPitch']
    stats_raw_combined.loc[file_name, 'max_rawRoll'] = stats_raw.loc['max', 'rawRoll']

    stats_filtered_combined.loc[file_name, 'mean_filteredYaw'] = stats_filtered.loc['mean', 'filteredYaw']
    stats_filtered_combined.loc[file_name, 'mean_filteredPitch'] = stats_filtered.loc['mean', 'filteredPitch']
    stats_filtered_combined.loc[file_name, 'mean_filteredRoll'] = stats_filtered.loc['mean', 'filteredRoll']
    stats_filtered_combined.loc[file_name, 'std_filteredYaw'] = stats_filtered.loc['std', 'filteredYaw']
    stats_filtered_combined.loc[file_name, 'std_filteredPitch'] = stats_filtered.loc['std', 'filteredPitch']
    stats_filtered_combined.loc[file_name, 'std_filteredRoll'] = stats_filtered.loc['std', 'filteredRoll']
    stats_filtered_combined.loc[file_name, 'min_filteredYaw'] = stats_filtered.loc['min', 'filteredYaw']
    stats_filtered_combined.loc[file_name, 'min_filteredPitch'] = stats_filtered.loc['min', 'filteredPitch']
    stats_filtered_combined.loc[file_name, 'min_filteredRoll'] = stats_filtered.loc['min', 'filteredRoll']
    stats_filtered_combined.loc[file_name, 'max_filteredYaw'] = stats_filtered.loc['max', 'filteredYaw']
    stats_filtered_combined.loc[file_name, 'max_filteredPitch'] = stats_filtered.loc['max', 'filteredPitch']
    stats_filtered_combined.loc[file_name, 'max_filteredRoll'] = stats_filtered.loc['max', 'filteredRoll']

    # 2D 데이터 시각화 및 저장
    fig, ax = plt.subplots(2, 1, figsize=(12, 10))
    ax[0].plot(df['scaled_time'], df['rawYaw'], label='Raw Yaw', color='blue')
    ax[0].plot(df['scaled_time'], df['rawPitch'], label='Raw Pitch', color='green')
    ax[0].plot(df['scaled_time'], df['rawRoll'], label='Raw Roll', color='red')
    ax[0].legend()
    ax[1].plot(df['scaled_time'], df['filteredYaw'], label='Filtered Yaw', color='blue')
    ax[1].plot(df['scaled_time'], df['filteredPitch'], label='Filtered Pitch', color='green')
    ax[1].plot(df['scaled_time'], df['filteredRoll'], label='Filtered Roll', color='red')
    ax[1].legend()
    plt.savefig(f'{save_directory}/{file_name}_2d_plot.png')
    plt.close(fig)  # 창을 닫아 다음 파일에 대한 그림이 제대로 생성되도록 합니다.

    # Raw data 3D 시각화 및 저장
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(df['rawYaw'], df['rawPitch'], df['rawRoll'], label='Raw Data', color='blue')
    ax.set_xlabel('Yaw')
    ax.set_ylabel('Pitch')
    ax.set_zlabel('Roll')
    ax.legend()
    plt.savefig(f'{save_directory}/{file_name}_raw_3d_plot.png')
    plt.close(fig)  # 창을 닫아 다음 파일에 대한 그림이 제대로 생성되도록 합니다.

    # Filtered data 3D 시각화 및 저장
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(df['filteredYaw'], df['filteredPitch'], df['filteredRoll'], label='Filtered Data', color='red')
    ax.set_xlabel('Yaw')
    ax.set_ylabel('Pitch')
    ax.set_zlabel('Roll')
    ax.legend()
    plt.savefig(f'{save_directory}/{file_name}_filtered_3d_plot.png')
    plt.close(fig)  # 창을 닫아 다음 파일에 대한 그림이 제대로 생성되도록 합니다.

# tkinter GUI를 사용하여 여러 파일 선택
Tk().withdraw()
file_paths = askopenfilenames() # 여러 파일 선택 다이얼로그를 표시

# 저장 위치 선택
save_directory = askdirectory(title='분석 결과 저장 위치 선택')

# 통합된 통계값을 저장할 데이터프레임 생성
stats_raw_combined = pd.DataFrame(columns=['mean_rawYaw', 'mean_rawPitch', 'mean_rawRoll', 
                                           'std_rawYaw', 'std_rawPitch', 'std_rawRoll',
                                           'min_rawYaw', 'min_rawPitch', 'min_rawRoll',
                                           'max_rawYaw', 'max_rawPitch', 'max_rawRoll'])
stats_filtered_combined = pd.DataFrame(columns=['mean_filteredYaw', 'mean_filteredPitch', 'mean_filteredRoll', 
                                                'std_filteredYaw', 'std_filteredPitch', 'std_filteredRoll',
                                                'min_filteredYaw', 'min_filteredPitch', 'min_filteredRoll',
                                                'max_filteredYaw', 'max_filteredPitch', 'max_filteredRoll'])

# 각 파일별 분석 및 저장
for file_path in file_paths:
    analyze_and_save(file_path, save_directory, stats_raw_combined, stats_filtered_combined)

# 통합된 통계값 저장
stats_raw_combined.to_csv(f'{save_directory}/stats_raw_combined.csv')
stats_filtered_combined.to_csv(f'{save_directory}/stats_filtered_combined.csv')