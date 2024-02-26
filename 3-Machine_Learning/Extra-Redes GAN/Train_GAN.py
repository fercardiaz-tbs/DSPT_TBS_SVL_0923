# 
from IPython import get_ipython


# Este modelo de Machine Learning, se utilizara una red neuronal GAN en imagenes de anime

# Para este modelo primero comenzaré con el dataset de MAL sin los usuarios ya que en el mismo 
# estan los puntajes dados por ellos sin los los datos personales que no nos importarian mucho

# ## Librerias

import sys 
import os
os.chdir(os.path.dirname(__file__))
from Utils.Librerias import *
from Utils.Path import *
from Utils.Visualizacion import *
from Utils.Limpieza import *
init_notebook_mode(connected=True)
cf.go_offline()


# ## GPU Activo?

print("Num GPUs Aviable: ", len(tf.config.list_physical_devices('GPU')))
if tf.test.gpu_device_name():
    print('Default GPU Device:' .format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")

# ## Activar toda la memoria del GPU

physical_devices = tf.config.list_physical_devices('GPU') 
for gpu_instance in physical_devices: 
    tf.config.experimental.set_memory_growth(gpu_instance, True)


# # ## Reshape images

def Reshape_img(Folder_input, Folder_output):
    st = time.time()

    cwsinput = Folder_input
    img_input_dir = cwsinput
    files = glob(img_input_dir)
    print(len(files))

    cwdoutput = os.getcwd() + Folder_output
    img_output_dir =cwdoutput
    imagesize = (128,128)
    for i,f1 in enumerate(files):
        startindex = f1.find(GANs)
        tempf1 = f1[startindex:]
        tempfn = img_output_dir + tempf1
        inputimage = cv2.imread(f1)
        sizedimage = cv2.resize(inputimage, imagesize)
        n = str(i) 
        cv2.imwrite(os.path.join(Folder_output, ('image'+ n +'.png')), sizedimage)
        
    print('The program took %s seconds' %(time.time()-st))

# ## Data Load
# A#adimos los datos en forma de numpy array

def Img_to_array(Folder_output):

    st = time.time()
    cwdinput = Folder_output+'\*.png'
    img_input_dir = cwdinput
    files = glob(img_input_dir)
    print(len(files))


    X_data = []
    iterations = 0
    for myFile in files:
        image = cv2.imread(myFile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        X_data.append(image)
        iterations = iterations + 1
        if(iterations % 1000 == 0):
            print(iterations)
        if(iterations == 7000):
            break

    X_data_array = np.asarray(X_data)
    print('X_data shape: ', X_data_array.shape)

    print('The program took %s seconds ' %(time.time()-st))

# save dataset

def save_array(data):

    filename = 'SRC\Model\Train_dataset_3.npz'
    savez_compressed(filename, data)
    print('Saved dataset: ', filename)


# ## Discriminator

def discriminator(in_shape=(128,128,3)):
	model = Sequential()
	model.add(Conv2D(64, (3,3), strides=(2, 2), padding='same', input_shape=in_shape))
	model.add(LeakyReLU(alpha=0.2))
	model.add(Conv2D(128, (3,3), strides=(2, 2), padding='same'))
	model.add(LeakyReLU(alpha=0.2))
	model.add(Conv2D(256, (3,3), strides=(2, 2), padding='same'))
	model.add(LeakyReLU(alpha=0.2))
	model.add(Conv2D(512, (3,3), strides=(2, 2), padding='same'))
	model.add(LeakyReLU(alpha=0.2))
	model.add(Flatten())
	model.add(Dropout(0.4))
	model.add(Dense(1, activation='sigmoid'))
	opt = Adam(lr=0.0002, beta_1=0.5)
	model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'], run_eagerly=True)
	return model

# ## Generator

def generator(latent_dim):
    model = Sequential()
    n_nodes = 8 * 8 * 512
    model.add(Dense(n_nodes, input_dim = latent_dim))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Reshape((8,8,512)))
    model.add(Conv2DTranspose(256, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2DTranspose(64, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2DTranspose(32, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(3, (3,3), activation='tanh', padding='same'))
    return model

# Funcion para a#adir al GAN 

def add_to_gan(g_model, d_model):
    d_model.trainable = False
    model = Sequential()
    model.add(g_model)
    model.add(d_model)
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt, run_eagerly=True)
    return model

# Normalizar los array

def load_real_samples():
    data = np.load('SRC\Model\Train_dataset_3.npz', allow_pickle=True)
    X = data['arr_0']
    X = X.astype('float32')
    X = (X - 127.5) / 127.5
    return X

# Ejemplos Reales para comparar

def generate_real_samples(dataset, n_samples):
    ix = randint(0, dataset.shape[0], n_samples)
    X = dataset[ix]
    y = ones((n_samples, 1))
    return X, y

# genera un punto latente 

# En el caso de las GAN, la red generadora aplica significado a los puntos 
# en un espacio latente elegido, de modo que los nuevos puntos extraídos del 
# espacio latente pueden proporcionarse a la red generadora como entrada y usarse 
# para generar ejemplos de salida nuevos y diferentes.

# ejemplo Una red generadora toma un punto de 100 dimensiones en el espacio latente como 
# entrada y genera una salida de 28x28x3. El punto en el espacio latente es un vector de números 
# aleatorios gaussianos. Esto se proyecta utilizando una capa densa en base a 64 pequeñas imágenes de 7 × 7.

def generate_latent_points(latent_dim, n_samples):
    x_input = randn(latent_dim * n_samples)
    x_input = x_input.reshape(n_samples, latent_dim)
    return x_input

# genera ejemplos falsos que es nuestro target

def generate_fake_samples(g_model, latent_dim, n_samples):
    x_input = generate_latent_points(latent_dim, n_samples)
    X = g_model.predict(x_input)
    y = zeros((n_samples, 1))
    return X, y

# guardamos el un plot de nuestras imagenes generadas cada 10 iteraciones

def save_plot(examples, epoch, n=4):
    examples = (examples + 1) / 2.0
    for i in range(n * n):
        plt.subplot(n, n, 1 + i)
        plt.axis('off')
        plt.imshow(examples[i])
    filename = R'SRC\Notebooks\plot\img%03d.png' %(epoch+1)
    plt.savefig(filename)
    plt.close();

# guardamos el modelo entrenado cada 10 iteraciones para llevar un registro

def summarize_performance(epoch, g_model, d_model, dataset, latent_dim, n_samples=150):
    X_real, y_real = generate_real_samples(dataset, n_samples)
    _, per_real = d_model.evaluate(X_real, y_real, verbose=0)
    x_fake, y_fake = generate_fake_samples(g_model, latent_dim, n_samples)
    _, per_fake = d_model.evaluate(x_fake, y_fake, verbose=0)
    print('Accuracy real: %.0f%%, fake: %.0f%%' % (per_real*100, per_fake*100))
    save_plot(x_fake, epoch)
    filename = R'SRC\Notebooks\plot\model%03d.h5' %(epoch+1)
    g_model.save(filename)

# funciones que utiliza las anteriones funciones para entrenar el modelo

def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=200, n_batch=32):
    bat_per_epo = int(dataset.shape[0] / n_batch)
    half_batch = int(n_batch / 2)
    for i in range(n_epochs):
        for j in range(bat_per_epo):
            X_real, y_real = generate_real_samples(dataset, half_batch)
            d_loss1, _ = d_model.train_on_batch(X_real, y_real)
            X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
            d_loss2, _ = d_model.train_on_batch(X_fake, y_fake)
            X_gan = generate_latent_points(latent_dim, n_batch)
            y_gan = ones((n_batch, 1))
            g_loss = gan_model.train_on_batch(X_gan, y_gan)
            print('>%d, %d/%d, d1=%.3f, d2=%.3f g=%.3f' % (i+1, j+1, bat_per_epo, d_loss1, d_loss2, g_loss))
        if (i + 1) % 10 == 0:
            summarize_performance(i, g_model, d_model, dataset, latent_dim)    


def GAN(latent_dim = 3000):
    latent_dim = latent_dim
    d_model = discriminator()
    g_model = generator(latent_dim)
    gan_model = add_to_gan(g_model, d_model)
    dataset = load_real_samples()
    train(g_model, d_model, gan_model, dataset, latent_dim)

def borrar_cache_GPU():
    from keras import backend as K
    K.clear_session()


Img_to_array(Folder_output)
GAN()