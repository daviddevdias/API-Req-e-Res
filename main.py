from spotify import buscar_musica


resultado = buscar_musica("Numb Linkin Park")


musicas = resultado["tracks"]["items"]


for musica in musicas:

    nome = musica["name"]
    artista = musica["artists"][0]["name"]
    link = musica["external_urls"]["spotify"]

    print("----------------")
    print("🎵", nome)
    print("👤", artista)
    print("🔗", link)