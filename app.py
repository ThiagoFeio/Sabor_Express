from modelos.restaurante import Restaurante

restaurante_las = Restaurante('las vegas','americana')
restaurante_japa = Restaurante('japa','japonesa')
restaurante_mex = Restaurante('mexican food ','mexicana')
restaurante_las.adicionar_avaliacao('Thiago',7)
restaurante_las.adicionar_avaliacao('Daniel',8)
restaurante_mex.adicionar_avaliacao('Alyen', 5)
restaurante_mex.adicionar_avaliacao('Alyne', 6)
Restaurante.alternar_estado(restaurante_mex)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

