x0 = keras.layers.concatenate((main_input, site_input, access_input))
x = Dense(200, activation="relu", kernel_initializer="lecun_uniform",
kernel_regularizer=regularizers.l2(regularizer))(x0)
x = Dropout(dropout)(x)
x = keras.layers.concatenate((x0, x))
x = Dense(200, activation="relu", kernel_initializer="lecun_uniform",
kernel_regularizer=regularizers.l2(regularizer))(x)
x = BatchNormalization(beta_regularizer=regularizers.l2(regularizer),
gamma_regularizer=regularizers.l2(regularizer))
x = Dropout(dropout)(x)
x = Dense(100, activation="relu", kernel_initializer="lecun_uniform",
kernel_regularizer=regularizers.l2(regularizer))(x)
x = Dropout(dropout)(x)
x = Dense(200, activation="relu", kernel_initializer="lecun_uniform",
kernel_regularizer=regularizers.l2(regularizer))(x)
x = Dropout(dropout)(x)
x = Dense(output_dim, activation="linear", kernel_initializer="lecun_uniform",
kernel_regularizer=regularizers.l2(regularizer))(x)
