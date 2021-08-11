class Weapon:
    def __init__(self, bullets=0):
        self.bullets = bullets

    def __repr__(self):
        return f"Remaining bullets: {repr(self.bullets)}"

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        elif self.bullets == 0:
            return "no bullets left"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
