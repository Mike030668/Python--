import tensorflow as tf
import numpy as np


class Unet_const:
    """
    Класс, являющийся конструктором Unet подобных сетей, позволяющий для любого
    размера входного изображения автоматически вычеслит как количество уровней, так
    и соответствующие каждому уровню filters и strides, чтобы размер в botelnec
    был (1,1).
    Но можно и уазать нужное количество уровней (не более автоматического) или
    прямо указать размеры фильтров для уровней. В этом случае будет создана сеть
    с подбором strides, чтобы размер botelnec был минимален для заданного к-ва
    уровней или указанных  filters
    Так же возможно выбрать какие предобученные сети (на ImageNet) использывать
    в энкодере VGG_16, VGG_19 или InceptionResNetV2.
    Можно уазать тренировать или нет предобученные слои.
    Можно уазывать многие параметры сети в отдельности на каждом уровне, передавая
    параметры кортежом.
    Много вариантность конструирования сети позволяет создать генетический алгоритм
    для подбора оптимальных параметров под задачу
    ----- base parametrs --------------------------------------------------------------
    image_shape - Полная размерность входного изображения 9к-во каналов на -1 индексе)
    num_classses - количество сегментов или классов на выходе int
    low_degree - минимальная значение для степени в высчитывании алгоритмом нужных
                 значений фильтров для уровней сети int. В коде заложен жестко ограничитель
                 на максимальное значение фильтра в 1024
    levels - если None, то высчитывается автоматически кодом c filters и strides,
             чтобы размер botelnec был (1,1);
             если int, то задает колиество уровней;
             если кортеж int, то len() кортежа это количество уровней, а значения
             это заданные фильтры.
             Во 2м и 3м случае размер botelnec уже не будет (1,1)
    residual - если False или True, то на всех уровнях энкодера и декодера не будет
              или соответстенно будут реализованы резидеал пробросы.
              Если кортеж из False или True, то резидиал будет реализован по индексам
              где True зеркально симметрично в энкодера и декодера, причем если
              количество уровней больше, чем указано, то далее берется значение
              по индесу -1
    kernel_initializer - возможно задать тип инициализации в сверточных слоях
                         отличный от базового
    kernel_regularizer - возможно задать тип регуляризации в сверточных слоях
                         отличный от базового
    out_activ - функция активации для выходного сверточного слоя
    pretatrain_net - если не False, то можно выбрать тип обученной сети на ImageNet
                     из которой возьмуться необходимые слии для энкодера.
                     Выбрать можно из  'vgg_16',  'vgg_19' и 'IncResNetV2'
                     для входов сетей есть некоторые ограничения, поэтому если
                     размерность входного изображения не проходит проверку, то будет
                     создана автоматически сеть без слоев предобученной сети
                     о чем выпадет сообщение
    train_pretrain_lays - разморозить слои обученной сети если True или заморозить
                          если False (будут тренироваться только новые слои)
    ----- encoder --------------------------------------------------------------
    enc_dropout - По умолчание False, если нужен dropout в энкодере, то нужно передать
                  кортеж кортежей((тип, rate)), где:
                  тип - 'Dropout' или 'Spatial'
                  rate - число от 0 до 1
                  То есть можно указать тип и размер дропаута каждому уровню, причем
                  если количество уровней больше, чем указано, то далее берется
                  значение по индесу -1
    enc_pool - нужно указать кортеж из'Maxpool' для MaxPooling2D и 'Avrpool' для AvgPool2D
               в енкодере. То есть можно указать тип пулинга каждому уровню, причем
               если количество уровней больше, чем указано, то далее берется
               значение по индесу -1
    enc_qtyconv - кортеж из одного или нескольких int, понимается как кколичество
                  сверточных блоков на каждом уровне энкодера, причем  если
                  количество уровней больше, чем указано, то далее берется
                  значение по индесу -1
    enc_kernels - кортеж из кортежей фильтров применяемых к входному массиву
                  сверточных блоков на соответствующем уровне энкодера, причем
                  если количество уровней  больше, чем указано, то далее берется
                  значение по индесу -1
    enc_activ - кортеж из строчных имен типов активационных функций, применяемых
                на соответствующем уровне энкодера, , причем  если количество уровней
                больше, чем указано, то далее берется  значение по индесу -1
    enc_usebtchnorm - кортеж из False или True, использывать или нет BatchNormalization
                      в сверточном блоке на соответствующем уровне энкодера, причем
                      если количество уровней  больше, чем указано, то далее берется
                      значение по индесу -1
    ----- botelnec --------------------------------------------------------------
    btlnec_qtyconv - int понимается как количество сверточных блоков в botelnec
    btlnec_kernels - кортежей фильтров применяемых к входному по массиву сверточных
                     слоев в botelnec
    btlnec_activ - тип активационной функции, применяемой в botelnec
    btlnec_usebtchnorm - спользывать или нет BatchNormalization в сверточном блоке
                         в botelnec
    ----- decoder --------------------------------------------------------------
    dec_uplayer - нужно указать кортеж из 'Conv2DT' для Conv2DTranspose и 'UpSampl'
                  для UpSampling2D в декодере. То есть можно указать тип апсемплинга
                  каждому уровню декодера, причем если количество уровней больше,
                  чем указано, то далее берется значение по индесу -1
    dec_qtyconv - кортеж из одного или нескольких int, понимается как кколичество
                  сверточных блоков на каждом уровне декодера, причем  если
                  количество уровней больше, чем указано, то далее берется
                  значение по индесу -1
    dec_kernels - кортеж из кортежей фильтров применяемых к входному массиву
                  сверточных блоков на соответствующем уровне декодера, причем
                  если количество уровней больше, чем указано, то далее берется
                  значение по индесу -1
    dec_activ - кортеж из строчных имен типов активационных функций, применяемых
                на соответствующем уровне декодера, , причем  если количество уровней
                больше, чем указано, то далее берется  значение по индесу -1
    dec_usebtchnorm - кортеж из False или True, использывать или нет BatchNormalization
                      в сверточном блоке на соответствующем уровне декодера, причем
                      если количество уровней  больше, чем указано, то далее берется
                      значение по индесу -1
    """

    def __init__(self,
                 image_shape,
                 num_classses,
                 low_degree=2,
                 levels=None,
                 residual=False,
                 kernel_initializer='glorot_uniform',
                 kernel_regularizer=None,
                 out_activ='softmax',
                 #### using pretatrain net
                 pretatrain_net=False,
                 train_pretrain_lays=False,
                 #### encoder
                 enc_dropout=False,
                 enc_pool=('Maxpool'),
                 enc_qtyconv=(2),
                 enc_kernels=((3, 3)),
                 enc_activ=('relu'),
                 enc_usebtchnorm=(True),
                 #### botelnec
                 btlnec_qtyconv=2,
                 btlnec_kernels=(3, 3),
                 btlnec_activ='relu',
                 btlnec_usebtchnorm=True,
                 #### decoder
                 dec_uplayer=('Conv2DT'),
                 dec_qtyconv=(2),
                 dec_kernels=((3, 3)),
                 dec_activ=('relu'),
                 dec_usebtchnorm=(True),
                 ):

        self.image_shape = image_shape
        self.num_classses = num_classses
        self.low_degree = low_degree
        self.levels = levels
        self.residual = residual
        self.initializer = kernel_initializer
        self.regularizer = kernel_regularizer
        self.pretatrain_net = pretatrain_net
        self.trainable = train_pretrain_lays
        self.dropout = enc_dropout
        self.enc_pool = enc_pool
        self.enc_qtyconv = enc_qtyconv
        self.enc_kernels = enc_kernels
        self.enc_activ = enc_activ
        self.enc_usebtchnorm = enc_usebtchnorm
        self.btlnec_qtyconv = btlnec_qtyconv
        self.btlnec_kernels = btlnec_kernels
        self.btlnec_activ = btlnec_activ
        self.btlnec_usebtchnorm = btlnec_usebtchnorm
        self.dec_qtyconv = dec_qtyconv
        self.dec_kernels = dec_kernels
        self.dec_activ = dec_activ
        self.dec_usebtchnorm = dec_usebtchnorm
        self.dec_uplayer = dec_uplayer
        self.out_activ = out_activ
        self.layers = tf.keras.layers

    def __call__(self):
        self.comment_1 = 'заданных' if self.levels else 'вычисленных'
        # Получаем список m_stride из простых множителей (simp_mult),
        # а также filters и количество уровне levels
        self.m_strides, self.filters, self.levels = self.__calculate_space_unet__(
            self.levels,
            self.low_degree
        )

        inputs = self.layers.Input(shape=self.image_shape)
        encoder_outs = self.__get_encoder__(inputs)

        bottleneck = self.__conv_block__(encoder_outs[-1][0],
                                         self.filters[-1],
                                         qty_conv=self.btlnec_qtyconv,
                                         kernels=self.btlnec_kernels,
                                         activ=self.btlnec_activ,
                                         usebatchnorm=self.btlnec_usebtchnorm
                                         )

        decoder_outs = self.__up_unetblocks__(bottleneck,
                                              encoder_outs,
                                              )

        outputs = self.layers.Conv2D(self.num_classses, (1, 1),
                                     activation=self.out_activ)(decoder_outs[-1])
        model = tf.keras.Model(inputs, outputs)

        return model

    def __get_encoder__(self, inputs):
        """
         Функция вычисляет выход энкодера в зависимости от ипользыания или нет
         предубоченных сетей, заданного или нет к-ва уровней/фильтров

         и выводит пояснение к сформированной сети
         """

        # контрольная степень 2 для предобученной сети и min_shape
        control = 7 if self.pretatrain_net == 'IncResNetV2' else 5
        min_shape = 128 if self.pretatrain_net == 'IncResNetV2' else 32

        comment_2 = 'тренеруемых' if self.trainable else 'замороженных'
        check_strides = np.array(self.m_strides)
        # если берем предобученные слои vgg и шейпы являются степенью двойки
        if self.pretatrain_net and np.all(check_strides[:control] == 2) and min(self.image_shape[:1]) >= min_shape:  #
            print(f'Сформирована сеть с использованием предобученных {comment_2} слоев {self.pretatrain_net}.\n'
                  f' \n'
                  f'Глубиной {self.levels} {self.comment_1} уровней.\n'
                  f' \n'
                  )
            encoder_outs = self.__douwn_pretrainlayers__(inputs)
        else:
            # выводим предупреждение если шейпы недля предобученных слоев
            if self.pretatrain_net and np.any(check_strides[:control] != 2) and min(self.image_shape[:1]) < min_shape:
                print(f'Внимание! \n'
                      f'Для использования предобученных слоев {self.pretatrain_net}, оба шейпа должны быть степенью 2 и не менее {2 ** control} пикселей! \n'
                      f' \n'
                      f'Сформирована сеть без предобученных слоев глубиной {self.levels} {self.comment_1} уровней.\n'
                      f' \n'
                      )
            else:
                print(f'Сформирована сеть с глубиной {self.levels} {self.comment_1} уровней.\n'
                      f' \n'
                      )

            encoder_outs = self.__douwn_unetblocks__(inputs)
        return encoder_outs

    def __bn_act__(self, x, batchnorm, activ=None):
        """ Batch Normalization & Activation """
        if batchnorm:
            x = self.layers.BatchNormalization()(x)
        if activ:
            input_name = x.name
            input_name = input_name.split('/')[0]
            number_lay = input_name.split('_')[-1]
            name_lay = f'{activ}_{number_lay}'
            x = self.layers.Activation(activ, name=name_lay)(x)
        return x

    def __conv_block__(self,
                       input_tensor,
                       num_filters,
                       qty_conv=2,
                       kernels=(3, 3),
                       activ='relu',
                       usebatchnorm=True
                       ):
        """
        Функция формирования сверточного блока.
        -----------------
        Входные данные:
        :param input_tensor: входной тензор;
        :param qty_conv: колиство слоев в блоке
        :param num_filters: кол-во сверточных фильтров блока;
        :param kernels: размер окна;
        :param activ: активационная функция;
        :param usebatchnorm: использывать или нет BatchNormalization;
        -----------------
        :return conv_block: выходной тензор.
        """
        # regularizer = tf.keras.regularizers.l1_l2(l1=0.001, l2=0.0001)
        for i in range(qty_conv):
            input = input_tensor if not i else conv_block
            conv_block = self.layers.Conv2D(num_filters, kernels,
                                            kernel_initializer=self.initializer,
                                            kernel_regularizer=self.regularizer,
                                            padding='same')(input)
            conv_block = self.__bn_act__(conv_block, usebatchnorm, activ)
        return conv_block

    def __residual__(self,
                     x,
                     out,
                     num_filters,
                     activ,
                     usebatchnorm
                     ):
        shortcut = self.layers.Conv2D(num_filters, kernel_size=(1, 1),
                                      padding='same', strides=1)(x)
        shortcut = self.__bn_act__(shortcut, usebatchnorm, activ)
        return self.layers.Add()([out, shortcut])

    def __encoder_block__(self,
                          input_tensor,
                          strides,
                          num_filters,
                          enc_pool,
                          qty_conv=2,
                          kernels=(3, 3),
                          activ='relu',
                          usebatchnorm=True,
                          ):
        """
        Функция формирования энкодер блока.
        -----------------
        Входные данные:
        input_tensor - входной тензор;
        strides - страйды из списка простых множителей
        qty_conv - колиство слоев в свертояном блоке
        num_filters - кол-во сверточных фильтров сверточного блока;
        enc_pool - тип пуллинга
        kernels - размер окна сверточного блока;
        activ - активационная функция сверточного блока;
        usebatchnorm - использывать или нет BatchNormalization в
                      сверточном блоке
        -----------------
        На выходе функции:
        encoder_pool - выходной тензор пулинга энкодера;
        encoder - выходной тензор свертки энкодера;
        """
        encoder = self.__conv_block__(input_tensor, num_filters, qty_conv,
                                      kernels, activ, usebatchnorm)
        if self.residual_level:
            encoder = self.__residual__(input_tensor, encoder, num_filters,
                                        activ, usebatchnorm)
        if self.dropout_level == 'Spatial':
            encoder = self.layers.SpatialDropout2D(self.rate_level)(encoder)

        pool = list(map(lambda x: min(2, x), strides))

        if enc_pool == 'Maxpool':
            encoder_pool = self.layers.MaxPooling2D(pool, strides)(encoder)

        elif enc_pool == 'Avrpool':
            encoder_pool = self.layers.AvgPool2D(pool, strides)(encoder)
        if self.dropout_level == 'Dropout':
            encoder_pool = self.layers.Dropout(self.rate_level)(encoder_pool)

        return encoder_pool, encoder

    def __decoder_block__(self,
                          input_tensor,
                          concat_tensor,
                          strides,
                          num_filters,
                          qty_conv=2,
                          kernels=(3, 3),
                          activ='relu',
                          usebatchnorm=True,
                          ):
        """
        Функция формирования декодер блока.
        -----------------
        Входные данные:
        input_tensor - входной тензор;
        concat_tensor - тензор для соединения
        strides - страйды из списка простых множителей
        qty_conv - количество слоев в сверточном блоке
        num_filters - кол-во сверточных фильтров сверточного блока;
        kernels - размер окна сверточного блока;
        activ - активационная функция сверточного блока;
        usebatchnorm - использывать или нет BatchNormalization в
                      сверточном блоке
        -----------------
        На выходе функции:
        decoder - выходной тензор свертки декодера;
        """

        if self.dec_uplayer_level == 'Conv2DT':
            decoder = self.layers.Conv2DTranspose(num_filters,
                                                  (2, 2),
                                                  strides,
                                                  kernel_initializer=self.initializer,
                                                  kernel_regularizer=self.regularizer,
                                                  padding='same')(input_tensor)
        elif self.dec_uplayer_level == 'UpSampl':
            decoder = self.layers.UpSampling2D(size=strides)(input_tensor)

        decoder = self.__bn_act__(decoder, usebatchnorm, activ)

        decoder = self.layers.concatenate([concat_tensor, decoder], axis=-1)

        decoder_out = self.__conv_block__(decoder, num_filters, qty_conv,
                                          kernels, activ, usebatchnorm)
        if self.residual_level:
            decoder_out = self.__residual__(decoder, decoder_out, num_filters,
                                            activ, usebatchnorm)
        return decoder_out

    def __simple_multipliers__(self, n):
        """
        Функция раскладывает число на простые множители
        -----------------
        :param n: натурально число
        -----------------
        :return: список всех простых множителей
        """
        ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            ans.append(n)
        return ans

    def __calculate_space_unet__(self,
                                 levels,
                                 low_degree):
        """
        Функция на основе простых множителей вычесляет количество
        уровней levels и фильтры filters, если они не заданы
        -----------------
        """
        # Разлагаем на простые множители минимальный размер изображения
        simp_mult = list(map(lambda x: self.__simple_multipliers__(x),
                             self.image_shape[:-1]))
        # Добиваем единицами меньшую размерность до равной длины
        qt_ones = abs(len(simp_mult[0]) - len(simp_mult[1]))
        if len(simp_mult[0]) > len(simp_mult[1]):
            simp_mult[1] += [1 for i in range(qt_ones)]
        elif len(simp_mult[0]) < len(simp_mult[1]):
            simp_mult[0] += [1 for i in range(qt_ones)]

            # Сортируем
        simp_mult = list(map(lambda x: sorted(x, reverse=True), simp_mult))
        # Поулучаем пары фильтров уровней
        simp_mult = [(i, j) for i, j in zip(simp_mult[0], simp_mult[1])]
        # Поулучаем кортеж максимальных фильрев уровней
        base = tuple(map(lambda x: max(x), simp_mult))

        # Получаем количество возможных уровней
        if not levels:  # если фильтры не заданы
            levels = len(simp_mult)

        # Если уровни заданы числом
        if type(levels) == int:
            # Создаем список степеней двойки от минимального
            degree_set = np.arange(low_degree, low_degree + levels)
            # Создаем фильтров
            filters = [min(1024, base[i] ** degree) for i, degree in enumerate(degree_set)]

            # если уровни заданы кортежом фильтров
        elif type(levels) == tuple:
            filters = levels
            levels = len(filters)

        return simp_mult, filters, levels

    def __get_atribute_level__(self, atribute, level):
        """
        Функция выдает арибт уровня из списка атрибута поровням.
        Если к-во уровней более длины списка, то далее выдает
        последний атрибут
        -----------------
        """
        qty_atribute = len(atribute) if atribute else 0
        if not atribute:
            atribute_level = atribute
        else:
            atribute_level = atribute[level] if level < qty_atribute else atribute[-1]
        return atribute_level

    def __zero_calc__(self,
                      d_shape):
        """
        Функция для определения zero падинга
        чтобы получить нужный формат слоя
        -----------------
        """
        base = d_shape // 2
        rest = d_shape % 2
        if rest:
            return (base + rest, base)
        else:
            return (base, base)

    def __douwn_pretrainlayers__(self, input_tensor, ):
        """
        Функция создает блок понижающей части Unet из
        предобученных слоев vgg_16, vgg_19, InceptionResNetV2
        -----------------
        """
        encoder_outs = []
        if self.pretatrain_net == 'vgg_16':
            vgg16 = tf.keras.applications.VGG16(include_top=False,
                                                weights='imagenet',
                                                input_tensor=input_tensor)
            vgg16.trainable = self.trainable
            for i in range(min(self.levels, 4)):
                j = 0 if i < 2 else 1
                encoder_pool = vgg16.get_layer('block' + str(i + 1) + '_pool').output
                encoder = vgg16.get_layer('block' + str(i + 1) + '_conv' + str(j + 2)).output
                encoder_outs.append([encoder_pool, encoder])

        if self.pretatrain_net == 'vgg_19':
            vgg19 = tf.keras.applications.vgg19.VGG19(include_top=False,
                                                      weights='imagenet',
                                                      input_tensor=input_tensor)
            vgg19.trainable = self.trainable
            for i in range(min(self.levels, 4)):
                j = 0 if i < 2 else 2
                encoder_pool = vgg19.get_layer('block' + str(i + 1) + '_pool').output
                encoder = vgg19.get_layer('block' + str(i + 1) + '_conv' + str(j + 2)).output
                encoder_outs.append([encoder_pool, encoder])

        if self.pretatrain_net == 'IncResNetV2':
            """ Pre-trained InceptionResNetV2 Model """
            InceptionResNetV2 = tf.keras.applications.InceptionResNetV2(include_top=False,
                                                                        weights="imagenet",
                                                                        input_tensor=input_tensor)
            InceptionResNetV2.trainable = self.trainable

            # Берем индексы слоев
            indexes = ((0, 1), (9, 10), (16, 17), (260, 273))
            for i in range(min(self.levels, 4)):
                encoder = InceptionResNetV2.get_layer(index=indexes[i][0]).output
                # Дополняем полученные карты 0 по перметру для выравнивания шйпов
                if i:
                    encoder = tf.keras.layers.ZeroPadding2D(
                        (self.__zero_calc__(encoder_outs[i - 1][0].shape[1] - encoder.shape[1]),
                         self.__zero_calc__(encoder_outs[i - 1][0].shape[2] - encoder.shape[2])))(encoder)

                encoder_pool = InceptionResNetV2.get_layer(index=indexes[i][1]).output
                encoder_pool = tf.keras.layers.ZeroPadding2D(
                    (self.__zero_calc__(encoder.shape[1] // 2 - encoder_pool.shape[1]),
                     self.__zero_calc__(encoder.shape[2] // 2 - encoder_pool.shape[2])))(encoder_pool)

                encoder_outs.append([encoder_pool, encoder])

        if self.levels > 4:
            # После предоубыченных, если идем глубже
            for i in range(4, self.levels):
                # Полуаем атрибуты уровня
                enc_activ_level = self.__get_atribute_level__(self.enc_activ, i)
                enc_usebatchnorm_level = self.__get_atribute_level__(self.enc_usebtchnorm, i)
                pooling_level = self.__get_atribute_level__(self.enc_pool, i)
                enc_qtyconv_level = self.__get_atribute_level__(self.enc_qtyconv, i)
                enc_kernels_level = self.__get_atribute_level__(self.enc_kernels, i)
                self.residual_level = self.__get_atribute_level__(self.residual, i)
                self.dropout_level, self.rate_level = self.__get_atribute_level__(self.dropout, i)

                encoder_pool, encoder = self.__encoder_block__(
                    encoder_outs[i - 1][0],
                    self.m_strides[i],
                    self.filters[i],
                    pooling_level,
                    enc_qtyconv_level,
                    enc_kernels_level,
                    enc_activ_level,
                    enc_usebatchnorm_level
                )
                encoder_outs.append([encoder_pool, encoder])

        return encoder_outs

    def __douwn_unetblocks__(self,
                             input_tensor,
                             ):
        """
        Функция создает блок понижающей части Unet
        -----------------
        """

        encoder_outs = []
        for i in range(self.levels):
            # Получаем атрибуты  по уровням энкодера
            enc_activ_level = self.__get_atribute_level__(self.enc_activ, i)
            enc_usebatchnorm_level = self.__get_atribute_level__(self.enc_usebtchnorm, i)
            pooling_level = self.__get_atribute_level__(self.enc_pool, i)
            enc_qtyconv_level = self.__get_atribute_level__(self.enc_qtyconv, i)
            enc_kernels_level = self.__get_atribute_level__(self.enc_kernels, i)
            self.residual_level = self.__get_atribute_level__(self.residual, i)
            self.dropout_level, self.rate_level = self.__get_atribute_level__(self.dropout, i)

            input = input_tensor if not i else encoder_outs[i - 1][0]
            encoder_pool, encoder = self.__encoder_block__(
                input,
                self.m_strides[i],
                self.filters[i],
                pooling_level,
                enc_qtyconv_level,
                enc_kernels_level,
                enc_activ_level,
                enc_usebatchnorm_level,
            )
            encoder_outs.append([encoder_pool, encoder])

        return encoder_outs

    def __up_unetblocks__(self,
                          input_tensor,
                          encoder_outs,
                          ):

        decoder_outs = []
        for i in reversed(range(self.levels)):
            # Получаем атрибуты  по уровням денкодера
            dec_activ_level = self.__get_atribute_level__(self.dec_activ, i)
            dec_usebatchnorm_level = self.__get_atribute_level__(self.dec_usebtchnorm, i)
            dec_qtyconv_level = self.__get_atribute_level__(self.dec_qtyconv, i)
            dec_kernels_level = self.__get_atribute_level__(self.dec_kernels, i)
            self.residual_level = self.__get_atribute_level__(self.residual, i)
            self.dec_uplayer_level = self.__get_atribute_level__(self.dec_uplayer, i)

            input = input_tensor if i == self.levels - 1 else decoder_outs[-1]
            decoder = self.__decoder_block__(
                input,
                encoder_outs[i][1],
                self.m_strides[i],
                self.filters[i],
                dec_qtyconv_level,
                dec_kernels_level,
                dec_activ_level,
                dec_usebatchnorm_level,
            )
            decoder_outs.append(decoder)
        return decoder_outs

if __name__ == '__main__':
    # Инициализация  сети
    num_classes = 1
    image_shape = (128, 128, 3)

    initializer = tf.keras.initializers.HeNormal()
    regularizer = tf.keras.regularizers.l1_l2(l1=0.001, l2=0.0001)

    model = Unet_const(image_shape,
                       num_classes,
                       low_degree=1,
                       levels=(3, 7, 17, 3, 7),  # 5, #5, #
                       kernel_regularizer=regularizer,
                       kernel_initializer=initializer,
                       residual=(True, False),
                       enc_dropout=(('Spatial', 0.1), ('Dropout', 0.3), ('Spatial', 0.3)),  #
                       enc_pool=('Maxpool', 'Avrpool', 'Avrpool', 'Avrpool', 'Maxpool'),
                       enc_activ=('selu', 'relu', 'tanh', 'elu'),  # None, #
                       enc_qtyconv=(1, 2, 3, 4),
                       enc_kernels=((2, 2), (3, 3)),
                       enc_usebtchnorm=(True, False, False, True, False),
                       dec_uplayer=('Conv2DT', 'UpSampl', 'UpSampl', 'Conv2DT'),
                       dec_usebtchnorm=(True, False, False, True, False),
                       dec_activ=('elu', 'sigmoid', 'tanh', 'selu'),  # None, #'selu',
                       dec_qtyconv=(1, 2, 3, 4),
                       dec_kernels=((3, 3), (2, 2)),
                       pretatrain_net='IncResNetV2',  # 'vgg_19', #
                       # train_pretrain_lays = False,
                       out_activ='sigmoid')()
    model.summary()