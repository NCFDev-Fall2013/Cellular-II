import threading,time,random
Thread = threading.Thread
 
def rand():
        return random.getrandbits(20)


class mediator():
	def __init__(self):
		self.listeners = []

	def register_listener(self,listener):
		self.listeners[listener]=1
		
	def unregister_listener(self, listener):
		if listener in self.listener.keys():
			self.listeners[listener]

        def request (request_from, request):
            if requester ==prn:
                request_from = grn
            else:
                request_from = prn                

            return request_from.eval(request)

 
class carrier:
        def __init__(self):
                self.lock = threading.Lock()
                self.value = None
 
def rs_write(rs, v):
        rs.lock.acquire()
        rs.value = v
        rs.lock.release()
def rs_append(rs, v):
        rs.lock.acquire()
        rs.value.append(v)
        rs.lock.release()
 
class grn(Thread, med):
        def __init__(self, history_c, curr_c, med):
                Thread.__init__(self)
          #      self.hist = history_c
          #      self.curr = curr_c

        # def send_request(desired_item):
        #if __name__ == "__main__":
        # curr = carrier()
        #history = carrier()
        #history.value = []
        #g = grn(history,curr)
        #p = prn(history,curr)
        #g.start()
        #p.start()
        #g.join()
        #p.join()
        #print history.value
        #print "\n".join( history.value )
        
	self.hist = med.request("prn", "hist")
        #self.curr = mediator.request(prn, curr)
        # def recieve_request(desired_item)


        def run(self):
                x = 0
                while x <= 100:
                        x += 1
                        G = rand()
                        rs_write(self.curr, G)
                        rs_append( self.hist, "{0}:\t{1}\t{2}".format(
                                time.time(), "g", G) )
                        time.sleep(1/10.)
                rs_append( self.hist, "{0}:\t{1}".format(
                                time.time(), "g-thread ended" ) )
class prn(threading.Thread, med):
        def __init__(self, history_c, curr_c,med):
                Thread.__init__(self)
           #     self.hist = history_c
           #     self.curr = curr_c

        self.hist = mediator.request("grn", "hist")
        self.curr = mediator.request("grn", "curr")

        def run(self):
                x = 0
                while x <= 10:
                        time.sleep(1)
                        G = self.curr.value
                        print G
                        rs_append( self.hist, "{0}:\t{1}\t{2}".format(
                                time.time(), " p", G) )
                        x += 1
                rs_append( self.hist, "{0}:\t{1}".format(
                                time.time(), "p-thread ended" ) )

med = mediator()


                
#if __name__ == "__main__":
        # curr = carrier()
        #history = carrier()
        #history.value = []
g = grn(history,curr,med)
p = prn(history,curr,med)
g.start()
p.start()
g.join()
p.join()
print history.value
print "\n".join( history.value )
        
