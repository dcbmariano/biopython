# ATOMOS 
a.get_name()      # nome do atomo
a.get_id()        # id
a.get_coord()     # coordenadas atomicas
a.get_vector()    # coordenadas como vetor
a.get_bfactor()   # fator B 
a.get_occupancy() # ocupancia
a.get_altloc()    # localizacao alternativa
a.get_sigatm()    # parametros atomicos
a.get_anisou()    # fator B anisotropico
a.get_fullname()  # nome completo do atomo

# RESIDUOS
r.get_resname()   # retorna o nome do residuo
r.is_disordered() # 1 se atomos desordenados
r.get_segid()     # retorna o SEGID
r.has_id(name)    # testa se tem certo atomo