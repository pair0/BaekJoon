import paramiko
import threading

# SSH 연결 설정
def ssh_command(ip, port, user, passwd, command, result_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(ip, port=port, username=user, password=passwd)
        
        # SSH 명령 실행
        stdin, stdout, stderr = client.exec_command(command)
        
        # 결과를 파일에 저장
        with open(result_file, 'w') as f:
            for line in stdout:
                f.write(line.strip() + '\n')
                
        print(f"Results from {ip} have been saved to {result_file}")
    except Exception as e:
        print(f"Error connecting to {ip}: {str(e)}")
    finally:
        client.close()

# 결과 확인 함수
def read_result_file(file_path):
    file_data = []
    row_count = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                file_data.append(line.strip())
                row_count += 1
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
    
    return file_data, row_count

if __name__ == "__main__":
# 서버 목록
    servers = [
        {"ip": "server1_ip", "port": 22, "user": "your_username", "passwd": "your_password"},
        {"ip": "server2_ip", "port": 22, "user": "your_username", "passwd": "your_password"}
    ]

    # 실행할 스크립트
    script_command = "./Ubuntu_script.sh"

    # 각 서버의 결과를 저장할 파일 이름 설정
    result_files = ["result_server1.txt", "result_server2.txt"]

    # 스레드로 각 서버에서 스크립트 실행
    threads = []
    for i, server in enumerate(servers):
        thread = threading.Thread(target=ssh_command, args=(server["ip"], server["port"], server["user"], server["passwd"], script_command, result_files[i]))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 대기
    for thread in threads:
        thread.join()

    # 결과 확인
    for result_file in result_files:
        print(f"\nChecking results for {result_file}:\n")
        file_data, row_count = read_result_file(result_file)
        
        # 결과 데이터 출력
        for line in file_data:
            print(line)
        
        # 전체 라인 수 출력
        print(f"Total lines in {result_file}: {row_count}")
