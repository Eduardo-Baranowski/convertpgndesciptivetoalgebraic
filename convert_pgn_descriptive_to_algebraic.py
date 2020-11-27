lances = "1. P4R P4R 2. c4 g6 3. Nf3 Bg7 4. g3 d5 5. cxd5 Nxd5 6. e4 Nb6 7. Bg2 O-O 8. O-O Bg4 9. d5 e6 10. h3 Bxf3 11. Bxf3 exd5 12. exd5 Qd7 13. Bg2 Rd8 14. Nc3 c6 15. dxc6 Nxc6 16. Qxd7 Rxd7 17. Bxc6 bxc6 18. Be3 Rad8 19. Rfd1 Bxc3 20. Rxd7 Rxd7 21. bxc3 Nd5 22. Rd1 Kf8 23. c4 Nb6 24. Rxd7 Nxd7 25. Bxa7 Ne5 26. c5 Ke7 27. f4 Nd3 28. Kf1 Ke6 29. a4 Kd5 30. a5 Nxc5 31. Ke2 f5 32. Bxc5 Kxc5 33. Kd3 Kb5 34. Kd4 Kxa5 35. Kc5 Ka4 36. Kxc6 Kb4 37. Kd5 Kc3 38. g4 fxg4 39. hxg4 Kd3 40. f5 gxf5 41. gxf5 h5 42. f6 h4 43. f7 h3 44. f8=Q h2 45. Qh6 Kc3 46. Qxh2 Kd3 47.Qf2 Kc3 48. Qe2 Kb4 49. Qd3 Ka4 50. Qb1 Ka3 51. Kc4 Ka4 52. Qb4# 1-0"
lances = lances.split()


for i in range(len(lances)):
    #print(lances[i][0])
    lance = lances[i][0]    
    if lances[i][-1] == '.':
        numero = lances[i]
        brancas = lances[i+1]        
        if brancas[0] == 'P' and brancas[2] == 'R' :            
            brancas = 'e'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'BR':
            brancas = 'f'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'CR':
            brancas = 'g'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'TR':
            brancas = 'h'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'D' :            
            brancas = 'd'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'BD':
            brancas = 'c'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'CD':
            brancas = 'b'+brancas[1]
        if brancas[0] == 'P' and brancas[2] == 'TD':
            brancas = 'a'+brancas[1]
        negras = lances[i+2]
        if negras[0] == 'P' and negras[2] == 'R' and negras[1] == '4' :            
            negras = 'e'+str(int(negras[1])+1)
        if negras[0] == 'P' and negras[2] == 'BR':
            negras = 'f'+negras[1]
        if negras[0] == 'P' and negras[2] == 'CR':
            negras = 'g'+negras[1]
        if negras[0] == 'P' and negras[2] == 'TR':
            negras = 'h'+negras[1]
        if negras[0] == 'P' and negras[2] == 'D' :            
            negras = 'd'+negras[1]
        if negras[0] == 'P' and negras[2] == 'BD':
            negras = 'c'+negras[1]
        if negras[0] == 'P' and negras[2] == 'CD':
            negras = 'b'+negras[1]
        if negras[0] == 'P' and negras[2] == 'TD':
            negras = 'a'+negras[1]

        print(numero+ ' ' + brancas+ ' ' + negras)
        
