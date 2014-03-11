import pyglet

from game import load, resources
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Version 2: Basic Motion", x= 400, y= 575, anchor_x='center', batch=main_batch)

player_ship = pyglet.sprite.Sprint(img=resources.player_image, x=400, y=300)

asteroids = load.asteroids(3, player_ship.position)

@game_window.event
def on_draw():
    # Draw things here
    game_window.clear()
    
    player_ship.draw()
    for asferoid in asteroids:
        asteroid.draw()
        
    
    level_label.draw()
    score_label.draw()

if __name__ == "__main__":
    pyglet.app.run()
