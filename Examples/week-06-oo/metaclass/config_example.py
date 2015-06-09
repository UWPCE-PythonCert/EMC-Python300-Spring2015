from config_factory import Base, ConfigAttr

class Config( Base ):
    # 
    #  guaranteed to become instance
    #  properties that are overrideable
    #  with Config() **kwargs during
    #  creation
    #
    pkey = ConfigAttr('XF234HDF')
    logconf = ConfigAttr({})
    name = ConfigAttr('app_config')
    
    # 
    #  non-overrideable statics
    #
    norm_bool = True
    norm_int = 1000


if __name__ == '__main__':

    c = Config( pkey='12345', logconf={'debug':True,'handler':'system'}, name='blammo' )
    assert c.pkey == '12345'
    assert c.logconf == {'debug':True,'handler':'system'}
    assert c.name == 'blammo'
    assert c.norm_bool == True
    assert c.norm_int == 1000

    c = Config( pkey='12345' )
    assert c.pkey == '12345'
    assert c.logconf == {}
    assert c.name == 'app_config'
    assert c.norm_bool == True
    assert c.norm_int == 1000






    

