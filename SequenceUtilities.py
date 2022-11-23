
def seqDiff(_s1,_s2,_n):
    _d = {}
    for k in _n:
        in_s1 = k in _s1
        in_s2 = k in _s2
        s1_blank = not in_s1 or (in_s1 and _s1[k]=='-')
        s2_blank = not in_s2 or (in_s2 and _s2[k]=='-')

        if s1_blank and s2_blank:
            pass
        elif s1_blank and not s2_blank:
            _d[k] = ['-',_s2[k]]
        elif not s1_blank and s2_blank:
            _d[k] = [_s1[k],'-']
        elif not s1_blank and not s2_blank and _s1[k]!=_s2[k]:
            _d[k] = [_s1[k],_s2[k]]
    return _d

def getNumbering(_chain):
    #RETURNS THE NUMBERING (IN ORDER) OF THE CHAIN 
    #ASSUMES CHOTHIA NUMBERING
      if _chain=='L':
          #these are all the possible positions for the CHOTHIA VL numbering
          pos = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                    '15','16','17','18','19','20','21','22','23','24','25','26','27',
                    '28','29','30','30A','30B','30C','30D','30E','30F','30G','30H','30I','31','32','33',
                    '34','35','36','37','38','39','40','41','42','43','44','45','46','47',
                    '48','49','50','51','51A','52','52A','52B','52C','52D','53','54','55','56','57','58','59','60','61',
                    '62','63','64','65','66','67','68','68A','68B','68C','69','70','71','72','73','74','75',
                    '76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91',
                    '92','93','94','95','95A','95B','95C','95D','95E','95F','95G','95H','95I','95J','96','97','98','99',
                    '100','101','102','103','104','105','106','106A','107']
          
      elif _chain=='H':
          pos = ['0','1','2','3','4','5','6','6A','7','8','9','10','11','12','13','14','15','16','17','18','19',
                 '20','21','22','23','24','25','26','27','28','29','30','31','31A','31B','31C','31D',
                 '31E','31F','31G','31H','31I','31J', '32','33','34','35',
                 '36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','52A',
                 '52B','52C','52D','52E','52F','52G','52H','52I','52J','52K','52L','52M','52N','52O', '53','54','55','56','57','58','59','59A', '60','60A', '61','62','63','64','64A','65','66','67','68',
                 '69','70','71','72','73','73A','73B','73C','73D','73E','73F','73G','73H','74','75','76',
                 '76A','76B','76C','76D','76E','76F','76G','76H','76I', '77','78','79','80','81','82','82A','82B','82C','83',
                 '84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','100A','100B',
                 '100C','100D','100E','100F','100G','100H','100I','100J','100K','100L','100M','100N','100O','100P',
                 '100Q','100R','100S','100T','100U','100V','100W','100X','100Y','100Z',
                 '101','102','103','104','105','106','107','108','109','110','111','112','113']
      return pos

def getCDRPos(_loop,cdr_scheme='chothia'):
    #ASSUMES SEQUENCES ARE NUMBERED IN CHOTHIA SCHEME
    if cdr_scheme=='chothia':
        CDRS = {'L1F':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                  '15','16','17','18','19','20','21','22','23'],
                'L1':['24','25','26','27','28','29','30','30A','30B','30C','30D','30E','30F',
                      '30G','30H','30I','31','32','33','34'],
                'L2F':['35','36','37','38','39','40','41','42','43','44','45','46','47',
                  '48','49'],
                'L2':['50','51','51A','52','52A','52B','52C','52D','53','54','55','56'],
                'L3F':['57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75',
                      '76','77','78','79','80','81','82','83','84','85','86','87','88'],
                'L3':['89','90','91','92','93','94','95','95A','95B','95C','95D','95E','95F',
                      '95G','95H','95I','95J', '96','97'],
                'L4F':['98','99','100','101','102','103','104','105','106','106A','107'],
                
                'H1F':['0','1','2','3','4','5','6','6A','7','8','9','10','11','12','13','14','15','16','17','18','19',
               '20','21','22','23','24','25'],
                'H1':['26','27','28','29','30','31','31A','31B','31C','31D','31E','31F','31G','31H','31I','31J',
                      '32'],
                'H2F':['33','34','35',
               '36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51'],
                'H2':['52','52A','52B','52C','52D','52E','52F','52G','52H','52I','52J','52K','52L','52M','52N','52O',
                      '53','54','55','56'],
                'H3F':['57','58','59','59A','60','60A', '61','62','63','64','64A','65','66','67','68',
               '69','70','71','72','73','74','75','76','76A','76B','76C','76D','76E','76F','76G','76H','76I','77','78','79','80','81','82','82A','82B','82C','83',
               '84','85','86','87','88','89','90','91','92','93','94'],
                'H3':['95','96','97','98','99','100','100A','100B','100C','100D',
                     '100E','100F','100G','100H','100I','100J','100K','100L','100M','100N','100O','100P',
                     '100Q','100R','100S','100T','100U','100V','100W','100X','100Y','100Z','101','102'],
               'H4F':['103','104','105','106','107','108','109','110','111','112','113']}
    elif cdr_scheme=='kabat':
        CDRS = {'L1F':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                  '15','16','17','18','19','20','21','22','23'],
                'L1':['24','25','26','27','28','29','30','30A','30B','30C','30D',
                      '30E','30F','30G','30H','30I','31','32','33','34'],
                'L2F':['35','36','37','38','39','40','41','42','43','44','45','46','47',
                  '48','49'],
               'L2':['50','51','51A','52','52A','52B','52C','52D','53','54','55','56'],
               'L3F':['57','58','59','60','61',
                  '62','63','64','65','66','67','68','69','70','71','72','73','74','75',
                  '76','77','78','79','80','81','82','83','84','85','86','87','88'],
               'L3':['89','90','91','92','93','94','95','95A','95B','95C','95D','95E','95F','96','97'],
               'L4F':['98','99','100','101','102','103','104','105','106','106A','107'],
                
               'H1F':['0','1','2','3','4','5','6','6A','7','8','9','10','11','12','13','14','15','16','17','18','19',
               '20','21','22','23','24','25','26','27','28','29','30'],
               'H1':['31','31A','31B','31C','31D','31E','31F','31G','31H','31I','31J', '32','33','34','35'],
               'H2F':['36','37','38','39','40','41','42','43','44','45','46','47','48','49'],
               'H2':['50','51','52','52A','52B','52C','52D','52E','52F','52G','52H','52I','52J','52K','52L',
                     '52M','52N','52O', '53','54','55','56','57','58','59','60','60A', '61','62','63','64','64A','65'],
               'H3F':['66','67','68',
               '69','70','71','72','73','74','75','76','77','78','79','80','81','82','82A','82B','82C','83',
               '84','85','86','87','88','89','90','91','92','93','94'],
               'H3':['95','96','97','98','99','100','100A','100B','100C','100D','100E','100F','100G','100H',
                     '100I','100J','100K','100L','100M','100N','100O','100P','100Q','100R','100S','100T','100U',
                     '100V','100W','100X','100Y','100Z','101','102'],
               'H4F':['103','104','105','106','107','108','109','110','111','112','113']}
    elif cdr_scheme=='abm':
      CDRS = {'L1F':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                  '15','16','17','18','19','20','21','22','23'],
              'L1':['24','25','26','27','28','29','30','30A','30B','30C','30D',
                      '30E','30F','30G','30H','30I','31','32','33','34'],
              'L2F':['35','36','37','38','39','40','41','42','43','44','45','46','47',
                  '48','49'],
              'L2':['50','51','51A','52','52A','52B','52C','52D','53','54','55','56'],
              'L3F':['57','58','59','60','61',
                  '62','63','64','65','66','67','68','69','70','71','72','73','74','75',
                  '76','77','78','79','80','81','82','83','84','85','86','87','88'],
              'L3':['89','90','91','92','93','94','95','95A','95B','95C','95D','95E','95F','96','97'],
              'L4F':['98','99','100','101','102','103','104','105','106','106A','107'],

              'H1F':['0','1','2','3','4','5','6','6A','7','8','9','10','11','12','13','14','15','16','17','18','19',
               '20','21','22','23','24','25'],
              'H1':['26','27','28','29','30','31','31A','31B','31C','31D','31E','31F','31G','31H','31I','31J',
                      '32','33','34','35'],
              'H2F':['36','37','38','39','40','41','42','43','44','45','46','47','48','49'],
              'H2':['50','51','52','52A','52B','52C','52D','52E','52F','52G','52H','52I','52J','52K','52L',
                     '52M','52N','52O', '53','54','55','56','57','58'],
              'H3F':['59','60','60A', '61','62','63','64','64A','65','66','67','68',
                     '69','70','71','72','73','74','75','76','77','78','79','80','81','82','82A','82B','82C','83',
                     '84','85','86','87','88','89','90','91','92','93','94'],
              'H3':['95','96','97','98','99','100','100A','100B','100C','100D',
                     '100E','100F','100G','100H','100I','100J','100K','100L','100M','100N','100O','100P',
                     '100Q','100R','100S','100T','100U','100V','100W','100X','100Y','100Z','101','102'],
               'H4F':['103','104','105','106','107','108','109','110','111','112','113']}
    elif cdr_scheme=='imgt':
        ###THESE ARE IMGT CDRS IN IMGT NUMBERING
        CDRS = {'L1F':['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                  '15','16','17','18','19','20','21','22','23','24','25','26'],
              'L1':['27', '28', '29', '30', '31','32','32A', '32B', '32C', '32D', '32E', '32F', '32G', 
                      '32H', '32I', '32J','32K','32L', '32M', '32N', '32O', '32P', '32Q', '32R', '32S', 
                      '32T', '32U', '32V', '32W','32X', '32Y', '32Z','33Z', '33Y', '33X', '33W', '33V', 
                      '33U', '33T', '33S', '33R', '33Q', '33P', '33O', '33N', '33M', '33L','33K', '33J', 
                      '33I', '33H', '33G','33F', '33E', '33D', '33C', '33B', '33A','33','34', '35', '36', 
                      '37', '38'],
              'L2F':['39','40','41','42','43','44','45','46','47',
                  '48','49','50','51','52','53','54','55'],
              'L2':['56', '57', '58', '59', '60', '60A', '60B', '60C', '60D','60E', '60F', '60G', '60H',
                      '60I', '60J', '60K','60L', '60M', '60N', '60O', '60P', '60Q', '60R', '60S', '60T', '60U',
                      '60V', '60W','60X', '60Y', '60Z','61Z', '61Y', '61X', '61W', '61V', '61U', '61T', '61S', 
                      '61R', '61Q',  '61P', '61O', '61N', '61M', '61L','61K', '61J', '61I', '61H', '61G','61F', 
                      '61E', '61D', '61C', '61B', '61A','61','62', '63', '64', '65'],
              'L3F':['66','67','68','69','70','71','72','73','74','75',
                  '76','77','78','79','80','81','82','83','84','85','86','87','88',
                  '89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104'],
              'L3':['105','106','107','108','109','110','111','111A', '111B', '111C', '111D', '111E', 
              '111F', '111G', '111H', '111I', '111J', '111K', '111L', '111M', '111N', '111O', '111P', '111Q', 
              '111R', '111S', '111T', '111U', '111V', '111W', '111X', '111Y', '111Z',
              '112Z', '112Y', '112X', '112W', '112V', 
              '112U', '112T', '112S', '112R', '112Q', '112P', '112O', '112N', 
              '112M', '112L', '112K', '112J', '112I', '112H', '112G', '112F', '112E', '112D', '112C', '112B', '112A','112',
              '113','114','115','116','117'],
              'L4F':['118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129'],

              'H1F':['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                  '15','16','17','18','19','20','21','22','23','24','25','26'],
              'H1':['27', '28', '29', '30', '31','32','32A', '32B', '32C', '32D', '32E', '32F', '32G', 
                        '32H', '32I', '32J','32K','32L', '32M', '32N', '32O', '32P', '32Q', '32R', '32S', 
                        '32T', '32U', '32V', '32W','32X', '32Y', '32Z','33Z', '33Y', '33X', '33W', '33V', 
                        '33U', '33T', '33S', '33R', '33Q', '33P', '33O', '33N', '33M', '33L','33K', '33J', 
                        '33I', '33H', '33G','33F', '33E', '33D', '33C', '33B', '33A','33','34', '35', '36',
                        '37', '38'],
              'H2F':['39','40','41','42','43','44','45','46','47',
                  '48','49','50','51','52','53','54','55'],
              'H2':['56', '57', '58', '59', '60', '60A', '60B', '60C', '60D', '60E', '60F', '60G', '60H', 
                    '60I', '60J', '60K','60L', '60M', '60N', '60O', '60P', '60Q', '60R', '60S', '60T', 
                    '60U', '60V', '60W','60X', '60Y', '60Z','61Z', '61Y', '61X', '61W', '61V', '61U', 
                    '61T', '61S', '61R', '61Q', '61P', '61O', '61N', '61M', '61L','61K', '61J', '61I', 
                    '61H', '61G','61F', '61E', '61D', '61C', '61B', '61A','61','62', '63', '64', '65'],
              'H3F':['66','67','68','69','70','71','72','73','74','75',
                  '76','77','78','79','80','81','82','83','84','85','86','87','88',
                  '89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104'],
              'H3':['105','106','107','108','109','110','111','111A', '111B', '111C', '111D', '111E', 
                    '111F', '111G', '111H', '111I', '111J', '111K', '111L', '111M', '111N', '111O', '111P', '111Q', 
                    '111R', '111S', '111T', '111U', '111V', '111W', '111X', '111Y', '111Z',
                    '111AA','111BB','111CC','111DD','111EE','111FF','112FF','112EE','112DD','112CC','112BB','112AA',
                    '112Z', '112Y', '112X', '112W', '112V', 
                    '112U', '112T', '112S', '112R', '112Q', '112P', '112O', '112N', 
                    '112M', '112L', '112K', '112J', '112I', '112H', '112G', '112F', '112E', '112D', '112C', '112B', '112A','112',
                    '113','114','115','116','117'],
              'H4F':['118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129']}

    elif cdr_scheme=='north':
        CDRS = {'L1F': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], 
        'L1': ['24', '25', '26', '27', '28', '29', '30', '30A', '30B', '30C', '30D', '30E', '30F', '30G', '30H', '30I', '31', '32', '33', '34'], 
        'L2F': ['35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'], 
        'L2': ['49', '50', '51', '51A', '52', '52A', '52B', '52C', '52D', '53', '54', '55', '56'], 
        'L3F': ['57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88'], 
        'L3': ['89', '90', '91', '92', '93', '94', '95', '95A', '95B', '95C', '95D', '95E', '95F', '95G', '95H', '95I', '95J', '96', '97'], 
        'L4F': ['98', '99', '100', '101', '102', '103', '104', '105', '106', '106A', '107'], 
        'H1F': ['0', '1', '2', '3', '4', '5', '6', '6A', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'], 
        'H1': ['23', '24', '25', '26', '27', '28', '29', '30', '31', '31A', '31B', '31C', '31D', '31E', '31F', '31G', '31H', '31I', '31J', '32', '33', '34', '35'], 
        'H2F': ['36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49'], 
        'H2': ['50', '51', '52', '52A', '52B', '52C', '52D', '52E', '52F', '52G', '52H', '52I', '52J', '52K', '52L', '52M', '52N', '52O', '53', '54', '55', '56', '57', '58'],
         'H3F': ['59','59A', '60','60A', '61', '62', '63', '64', '64A', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76','76A','76B','76C','76D','76E','76F','76G','76H','76I', '77', '78', '79', '80', '81', '82', '82A', '82B', '82C', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92'], 
         'H3': ['93', '94', '95', '96', '97', '98', '99', '100', '100A', '100B', '100C', '100D', '100E', '100F', '100G', '100H', '100I', '100J', '100K', '100L', '100M', '100N', '100O', '100P', '100Q', '100R', '100S', '100T', '100U', '100V', '100W', '100X', '100Y', '100Z', '101', '102'], 
         'H4F': ['103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113']}

               
    return CDRS[_loop]

def seqID(_s1,_s2,_n=None):
    #_s1 dict or string sequence
    #_s2 dict or string sequence
    #if _s1, _s2 are dict, what positions we want to compare
    if type(_s1) is dict:
        if _n is None:
            raise ValueError('If sequences are in dict representation, must provide a numbering to compare.')
        tot = 0
        match = 0
        for i in _n:
            if i not in _s1 and i not in _s2:
                continue

            elif i in _s1 and i not in _s2:
                if _s1[i]!='-':
                    tot+=1
                continue
            elif i in _s2 and i not in _s1:
                if _s2[i]!='-':
                    tot+=1
                continue

            elif _s1[i]=='-' and _s2[i]!='-':
                tot+=1
                continue
            elif _s2[i]=='-' and _s1[i]!='-':
                tot+=1
                continue

            elif _s1[i]!='-' and _s2[i]!='-':
                tot+=1
                if _s1[i]==_s2[i]:
                    match+=1
    
        return match/tot

    elif type(_s1) is str:
        if len(_s1)!=len(_s2):
            raise ValueError('If sequences are str representation, must be of equal length')
        
        match = 0
        for i in range(len(_s1)):
            if _s1[i]==_s2[i]:
                match+=1
        
        return match/len(_s1)
