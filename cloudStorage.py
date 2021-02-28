
import dropbox 
class Transferdata:
    def __init__(self,at):
        self.accessToken = at
    def upload_file (self,source,destination)  :
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(source,'rb')
        dbx.files_upload(f.read(),destination)

def  main():
    a = 'EuyYeI105pgAAAAAAAAAAT_eq9WV-dLJcecv8g9xhf30TfBp-95ICgYYAhpli-Yw'
    t = Transferdata(a)
    s =  input ('enter the file path to transfer')
    i = input ('enter the path to upload to dropbox')
    t.upload_file(s,i)
    print ('file has been moved')

main()
        


            
