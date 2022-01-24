from multiprocessing import Pool, Process, Pipe
from aot_scraper.main import scrape

# def f(i,j, proc_send):
#     my_list = []
#     def y(z, b:int):
#         v = z+b
#         my_list.append(v)
#     a = y(i, j)
#     proc_send.send(my_list)


# def f(i,j):
#     my_list = []
#     def y(z, b:int):
#         v = z+b
#         my_list.append(v)
#     a = y(i, j)
#     return my_list


# my_list = []

# def y(z, b:int):
#         i = z+b
#         my_list.append(i)


# def f(i,j, proc_send):
    
#     a = y(i, j)
#     proc_send.send(a)

# def y(z, b:int):
#         i = z+b
#         return i

# def f(i,j, proc_send):
#     my_list = []
    
#     a = y(i, j)
#     proc_send.send(a)


# def scrape(spider: int):
#         scrape.var = [spider]
#         # self.scrape.var = [spider]
#         add_item()
#         return scrape.var

# def add_item():
#     scrape.var.append(3)


# def firstFunction():
#     firstFunction.var = 100
#     print(firstFunction.var)

# def secondFunction():
#     print(firstFunction.var + 100)

def sprinter(site):
    pool = Pool()
    args = [([site])]
    return pool.starmap(scrape, args)




if __name__ == '__main__':
    # pool = Pool()
    # args = [(12,13,),(13, 14)]
    # print(pool.starmap(f, args))
    # # pipe_list = []

    
    # recv_end, send_end = Pipe(False)
    # p = Process(target=f, args=(12, 13,send_end,))
    
    # pipe_list.append(recv_end)
    # p.start()
    # p.join()
    # result_list = [x.recv() for x in pipe_list]
    # print(result_list[0])
    # print(scrape(4))
    # firstFunction()
    # secondFunction()

    # pool = Pool()
    # args = [(12,13,),(13, 14)]
    # kwargs = [(4,)]
    # print(pool.starmap(scrape, kwargs))

    # Execution type 1
    # active_scraper = CustomCrawler()
    # Execution type 1
    # p = Process(target=active_scraper.scrape, args=([site.value],))
    # p.start()
    # p.join()

    # Execution type 2
    # pool = Pool()
    # args = [([[site.value]])]
    # return{"message": pool.starmap(active_scraper.scrape, args)}

    # Execution type 3
    # pipe_list = []
    # recv_end, send_end = Pipe(False)
    # p = Process(target=active_scraper.scrape, args=([site.value], send_end,))
    #
    # pipe_list.append(recv_end)
    # p.start()
    # p.join()
    # result_list = [x.recv() for x in pipe_list]
    # return {"scraped data": result_list[0]}
    print(sprinter(site="aot_titans"))


