
def set_session_config(per_process_gpu_memory_fraction=None, allow_growth=None, device_list='0'):
    """

    :param allow_growth: When necessary, reserve memory
    :param float per_process_gpu_memory_fraction: specify GPU memory usage as 0 to 1

    :return:
    """
    import tensorflow as tf
    import keras.backend as K

    tf.disable_v2_behavior()
    config = tf.ConfigProto(
        allow_soft_placement=True,
        gpu_options=tf.GPUOptions(
            per_process_gpu_memory_fraction=per_process_gpu_memory_fraction,
            allow_growth=allow_growth,
            visible_device_list=device_list
        )
    )
    sess = tf.Session(config=config)
    K.set_session(sess)
    return sess   # this return value is used by agent to set keras session
