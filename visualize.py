import matplotlib.pyplot as plt
from celluloid import Camera

from sounds_of_space.io import read_img

if __name__ == "__main__":
    fname = "data/t1143_mrrde_10n263_0256_3"
    data = read_img(fname).asarray()

    camera = Camera(plt.gcf())
    plt.axis("off")
    plt.tight_layout()

    for i in range(data.shape[2]):
        plt.imshow(data[..., i])
        camera.snap()
    animation = camera.animate()

    animation.save("gif.gif")
