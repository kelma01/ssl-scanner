import sslyze
from sslyze import ServerNetworkLocation, ServerScanResult, ServerScanRequest, Scanner

class SslyzeScanner:
    def __init__(self, domain):
        self.domain = domain

    def start_scan(self):
        scanner = Scanner()
        request = ServerScanRequest(server_location=ServerNetworkLocation(hostname=self.domain))
        scanner.queue_scans([request])
        for result in scanner.get_results():
            self.result_as_json(result)

    def result_as_json(self, result):
        pass

def main():
    # domain = input("Enter domain to start scan...")
    domain = 'google.com'
    ssl_scanner = SslyzeScanner(domain=domain)
    ssl_scanner.start_scan()


if __name__ == '__main__':
    main()