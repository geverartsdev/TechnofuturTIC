
#Partie à mettre dans le dossier __init__

sound_list = list()
sound_list.append("1.wav")
sound_list.append("1.wav")
sound_list.append("1.wav")
sound_list.append("1.wav")
def randomMusic():
    if pygame.mixer and SONS and not pygame.mixer.music.get_busy():
        music = os.path.join(main_dir, 'src/sound', sound_list[random.randint(0,4)])
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

def sons():
    """
    Cette methode s'occupe de charger les sons du jeu et lance la musique principale
    :return:
    """
    if pygame.mixer and SONS:
        music = os.path.join(main_dir, 'src/sound', '')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

def main():
    """
    Fonction principale, appelle lors de l'execution du script
    :return: ∅
    """
    # Initialisation de pygame
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None


    
