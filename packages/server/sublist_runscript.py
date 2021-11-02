import subprocess

output=subprocess.check_output(
    "python sublist3r.py -v -d arowex.com "
)


def get_subdomains(domain_name):
    
    """
     packet structure:
          {
              SSL Certificates + Subdomains -> not a dict (bytes format)
          }
    """
    
    command= f"python sublist3r.py -v -d {domain_name}"
    
    output=subprocess.check_output(
        command
    )
    
    return output
    
    


def run(domain_name:str):
    return (get_subdomains(domain_name))

if __name__=="__main__":
    print(run('arowex.com'))