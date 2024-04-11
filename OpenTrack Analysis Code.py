import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import os

def analyze_and_save(file_path, save_directory, stats_raw_combined, stats_filtered_combined):
    df = pd.read_csv(file_path)
    sampling_rate = 250
    df['scaled_time'] = df.index / sampling_rate

    stats_raw = df[['rawYaw', 'rawPitch', 'rawRoll']].agg(['mean', 'std', 'min', 'max'])
    stats_filtered = df[['filteredYaw', 'filteredPitch', 'filteredRoll']].agg(['mean', 'std', 'min', 'max'])

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    for col in ['Yaw', 'Pitch', 'Roll']:
        for stat in ['mean', 'std', 'min', 'max']:
            stats_raw_combined.loc[file_name, f'{stat}_raw{col}'] = stats_raw.loc[stat, f'raw{col}']
            stats_filtered_combined.loc[file_name, f'{stat}_filtered{col}'] = stats_filtered.loc[stat, f'filtered{col}']

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
    plt.close(fig)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(df['rawYaw'], df['rawPitch'], df['rawRoll'], label='Raw Data', color='blue')
    ax.set_xlabel('Yaw')
    ax.set_ylabel('Pitch')
    ax.set_zlabel('Roll')
    ax.legend()
    plt.savefig(f'{save_directory}/{file_name}_raw_3d_plot.png')
    plt.close(fig)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(df['filteredYaw'], df['filteredPitch'], df['filteredRoll'], label='Filtered Data', color='red')
    ax.set_xlabel('Yaw')
    ax.set_ylabel('Pitch')
    ax.set_zlabel('Roll')
    ax.legend()
    plt.savefig(f'{save_directory}/{file_name}_filtered_3d_plot.png')
    plt.close(fig)

def main():
    Tk().withdraw()
    file_paths = askopenfilenames()
    save_directory = askdirectory(title='분석 결과 저장 위치 선택')

    raw_columns = [f'{stat}_raw{col}' for stat in ['mean', 'std', 'min', 'max'] for col in ['Yaw', 'Pitch', 'Roll']]
    filtered_columns = [f'{stat}_filtered{col}' for stat in ['mean', 'std', 'min', 'max'] for col in ['Yaw', 'Pitch', 'Roll']]

    stats_raw_combined = pd.DataFrame(columns=raw_columns)
    stats_filtered_combined = pd.DataFrame(columns=filtered_columns)

    for file_path in file_paths:
        analyze_and_save(file_path, save_directory, stats_raw_combined, stats_filtered_combined)

    stats_raw_combined.to_csv(f'{save_directory}/stats_raw_combined.csv')
    stats_filtered_combined.to_csv(f'{save_directory}/stats_filtered_combined.csv')

if __name__ == '__main__':
    main()
