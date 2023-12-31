class Config(object):
    env = 'default'
    backbone = 'resnet100'
    classify = 'softmax'
    num_classes = 13938
    metric = 'arc_margin'
    easy_margin = False
    use_se = False
    loss = 'focal_loss'

    display = True
    finetune = False

    train_root = ''
    train_list = 'dataset\list_data_train.txt'

    test_root = ''
    test_list = 'dataset\list_data_val.txt'

    # test_root = ''
    # test_list = 'test.txt'

    lfw_root = '/data/Datasets/lfw/lfw-align-128'
    lfw_test_list = '/data/Datasets/lfw/lfw_test_pair.txt'

    checkpoints_path = 'weights'
    load_model_path = 'models/resnet18.pth'
    test_model_path = 'checkpoints/resnet18_110.pth'
    save_interval = 10

    train_batch_size = 32  # batch size
    test_batch_size = 32

    input_shape = (3, 112, 112)

    optimizer = 'sgd'

    use_gpu = True  # use GPU or not
    gpu_id = '0, 1'
    num_workers = 4  # how many workers for loading data
    print_freq = 100  # print info every N batch

    debug_file = '/tmp/debug'  # if os.path.exists(debug_file): enter ipdb
    result_file = 'result.csv'

    max_epoch = 200
    lr = 1e-3  # initial learning rate
    lr_step = 60
    lr_decay = 0.95  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 5e-4
