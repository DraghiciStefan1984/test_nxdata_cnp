from cnp import CNP
import datetime



if __name__=='__main__':
    cnp=CNP(gender='male', birthdate='2000-43-4', birthplace='ilfov', status='resident')
    print(cnp.create_CNP())
    print(cnp.birthdate)