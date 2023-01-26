
# Modules used to solve this problem
import numpy as np
from scipy.integrate import solve_ivp
import pygame

# Lorenze class object
class lorenz:
    def __init__(self, y0, sigma, rho, beta):
        self.y0 = y0
        self.tint = [0, 100]
        self.dt = 0.01
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    # Initializes Lorenz system
    def lorenz_system(self, t, y):
        x, y, z = y
        dydt = [self.sigma*(y-x), x*(self.rho-z)-y, x*y-self.beta*z]
        return dydt

# Pygame display class object
class plot:
    def __init__(self, size, *solutions):
        self.size = size
        self.solution = solutions

    # Generates pygame display and updates generating the solution point by point
    def game(self):
        pygame.init()
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Lorenz Attractor")
        colors = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]
        clock = pygame.time.Clock()

        font = pygame.font.Font("fonts/arial.ttf", 16)
        text0 = font.render(f"sigma: {np.round(10, 2)}", True, colors[0])
        text1 = font.render(f"rho: {np.round(28, 2)}", True, colors[0])
        text2 = font.render(f"beta: {np.round(8/3, 2)}", True, colors[0])
        screen.blit(text0, (50, 50))
        screen.blit(text1, (50, 70))
        screen.blit(text2, (50, 90))

        # Main loop
        running = True
        pressed_enter = False
        iargs = 0
        while running:
            # runs at 30 fps
            clock.tick(30)

            for event in pygame.event.get():
                # Quit Game
                if event.type == pygame.QUIT:
                    running = False        
                
                # Excecutes when the key is pushed down
                if event.type == pygame.KEYDOWN:
                    # Press enter to start
                    if event.key == pygame.K_s:
                        pressed_enter = True

                    # Press q to Quit Game
                    if event.key == pygame.K_q:
                            running = False

                    # Press r to reset game
                    if event.key == pygame.K_r:
                        running = False
                        pressed_enter = True 
                        self.game()
                             

            if pressed_enter:
                # generates 3 points at the locs: (x0, y0) (x1, y1) (x2, y2) for every update
                try:
                    x0 = int(self.size[0]/2 + self.solution[0].y[0][iargs]*10)
                    y0 = int(self.size[1]/2 + self.solution[0].y[1][iargs]*10)
                    x1 = int(self.size[0]/2 + self.solution[1].y[0][iargs]*10)
                    y1 = int(self.size[1]/2 + self.solution[1].y[1][iargs]*10)
                    x2 = int(self.size[0]/2 + self.solution[2].y[0][iargs]*10)
                    y2 = int(self.size[1]/2 + self.solution[2].y[1][iargs]*10)

                    iargs += 1
                    pygame.draw.circle(screen, colors[0], (x0, y0), 1)
                    pygame.draw.circle(screen, colors[1], (x1, y1), 1)
                    pygame.draw.circle(screen, colors[2], (x2, y2), 1)
                    pygame.display.flip()
                    pygame.time.wait(10)
                
                except IndexError:
                    running = False

        pygame.quit()


if __name__ == '__main__':
    print('PROGRAM STARTED')
    systems = [lorenz([np.random.uniform(0.99, 1.01), 
                        np.random.uniform(0.99, 1.01), 
                        np.random.uniform(0.99, 1.01)
                        ],
                        10, 
                        28, 
                        8/3) for _ in range(3)
                ]

    print(f'Initial Conditions:\n solution 1 x: {systems[0].y0[0]} y: {systems[0].y0[1]} z: {systems[0].y0[2]}\n solution 2 x: {systems[1].y0[0]} y: {systems[1].y0[1]} z: {systems[1].y0[2]}\n solution 3 x: {systems[2].y0[0]} y: {systems[2].y0[1]} z: {systems[2].y0[2]}')

    # Solution 1
    solution0 = solve_ivp(lambda t, y: systems[0].lorenz_system(t, y), 
                            systems[0].tint, systems[0].y0,
                            t_eval=np.arange(systems[0].tint[0], systems[0].tint[1], systems[0].dt)
                            )

    # Solution 2
    solution1 = solve_ivp(lambda t, y: systems[1].lorenz_system(t, y), 
                            systems[1].tint, systems[1].y0,
                            t_eval=np.arange(systems[1].tint[0], systems[1].tint[1], systems[1].dt)
                            )

    # Solution 3
    solution2 = solve_ivp(lambda t, y: systems[2].lorenz_system(t, y), 
                            systems[2].tint, systems[2].y0,
                            t_eval=np.arange(systems[2].tint[0], systems[2].tint[1], systems[2].dt)
                            )

    print('SYSTEM OF EQUATION SOLVED SUCCESSFULLY')
    visualization = plot((800, 600), solution0, solution1, solution2)
    print('PLOTTING OBJECT INITIALIZED SUCCESSFULLY')

    visualization.game()
    print('PYGAME RAN SUCCESSFULLY')
    print('-----------------------\nPROGRAMM RAN SUCCESSFULLY')

