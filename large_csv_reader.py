import csv
import time
import pickle
import gc

def readcsv2list(filename, rows, last_position, max_line):
    fileobj = open(filename, 'rt',encoding='utf-8')
    fileobj.seek(last_position)
    datalines = []
    for i in range(max_line):
        line_itme = fileobj.readline()
        if len(line_itme) > 0:
            datalines.append(line_itme)
        else:
            break
    csv.register_dialect('mydialect',delimiter='\t')
    csvreader = csv.reader(datalines,'mydialect')
    retlist = []
    for row in csvreader:
        clist = []
        selected_rows = [ic for ic in range(len(row)) if ic not in rows]
        for c in selected_rows:
            clist.append(row[c])
        retlist.append(clist)
    current_position = fileobj.tell()
    fileobj.close()
    return retlist, current_position

def loadfilelist(filename):
    filelist = pickle.load(open(filename,'rb'))
    return filelist

if __name__ == '__main__':
    filename = 'bs_student_network_record.csv',
    rows = []
    max_line = 1000000
    for name in filename:
        position = 0
        # locals()['filelist_' + filename[:-4]] = loadfilelist(filename[:-4]+'.txt')

        cnt = 1
        while True:
            time_start = time.time()
            locals()['filelist_' + name[:-4] + '_' + str(cnt)] = []
            locals()['filelist_' + name[:-4] + '_' + str(cnt)], position = readcsv2list(name,rows,position,max_line)
            if locals()['filelist_'+name[:-4]+'_'+str(cnt)]:
                pickle.dump(locals()['filelist_'+name[:-4]+'_'+str(cnt)], open(name[:-4]+'_'+str(cnt)+'.txt', 'wb'))
                del locals()['filelist_'+name[:-4]+'_'+str(cnt)]
                gc.collect()
                time_end = time.time()
                print('READ CSV totally cost', time_end - time_start)
                cnt = cnt + 1
            else:
                break

