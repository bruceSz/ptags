import os

class FileParser(object):

    def filesUnder(self,root):
        queue = []
        queue.append(root)

        files = []
        while len(queue)>0:
            cur = queue.pop()
            cur=cur.rstrip('/')
            for f in os.listdir(cur):

                full_name = cur+'/'+f
                if os.path.isdir(full_name):
                    queue.insert(0,full_name)
                else:
                    # there are also type like socket etc.
                    if os.path.isfile(full_name):
                        files.append(full_name)


        for index,f in enumerate(files):
            print f



    def is_target(self,fname):
        return True


if __name__ == '__main__':
    fp = FileParser()
    fp.filesUnder('/tmp')
