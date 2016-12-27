import time

__author__ = 'jiataogu'
import os
import os.path as path


def setup_keyphrase_all():
    config = dict()
    # config['seed']            = 3030029828
    config['seed']            = 19900226
    # config['task_name']       = 'keyphrase-irbooks.one2one.nocopy'
    config['task_name']       = 'copynet-keyphrase-all.one2one.copy'
    config['timemark']        = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['clipnorm']        = 0.01

    config['save_updates']    = True
    config['get_instance']    = True

    config['path']            = path.realpath(path.curdir)

    config['path_experiment'] = path.realpath(path.curdir) + '/Experiment/'+config['task_name']
    config['path_h5']         = config['path_experiment']
    config['path_log']        = config['path_experiment']

    config['casestudy_log']   = config['path_experiment'] + '/case-print.log'

    config['training_name']   = 'acm-sci-journal_600k'
    config['training_dataset']= config['path'] + '/dataset/keyphrase/million-paper/all_title_abstract_keyword_clean.json'
    config['testing_name']    = 'inspec_all'
    config['testing_dataset'] = config['path'] + '/dataset/keyphrase/inspec/inspec_all.json'

    config['testing_datasets']= ['inspec', 'nus', 'semeval']
    config['preprocess_type'] = 1 # 0 is old type, 1 is new type(keep most punctuation)

    config['dataset']         = config['path'] + '/dataset/keyphrase/all_600k_dataset.pkl'
    config['voc']             = config['path'] + '/dataset/keyphrase/all_600k_voc.pkl' # for manual check

    # output log place
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])

    # trained_model
    config['trained_model']   = path.realpath(path.curdir) + '/Experiment/' + 'copynet-keyphrase-all.one2one.copy/experiments.copynet-keyphrase-all.one2one.copy.id=20161220-070035.epoch=2.batch=10000.pkl'
    # A well-trained model on all data
    #   path.realpath(path.curdir) + '/Experiment/' + 'copynet-keyphrase-all.one2one.nocopy.<eol><digit>.emb=100.hid=150/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161129-195005.epoch=2.pkl'
    # A well-trained model on acm data
    # config['path_experiment'] + '/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161129-195005.epoch=2.pkl'
    config['weight_json']= config['path_experiment'] + '/model_weight.json'
    config['resume_training'] = True
    config['training_archive']= config['path_experiment'] + '/save_training_status.id=20161220-070035.epoch=2.batch=10000.pkl'
        #config['path_experiment'] + '/save_training_status.pkl'

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 10
    config['mini_batch_size'] = 10
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = 50000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 150    # 100
    config['enc_hidden_dim']  = 300    # 150
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 150  # 100
    config['dec_hidden_dim']  = 300  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = True
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']


    # Decoder: sampling
    config['multi_output']    = False
    config['max_len']         = 8
    config['sample_beam']     = 50
    config['sample_stoch']    = False # use beamsearch
    config['sample_argmax']   = False

    config['predict_type']    = 'extractive' # type of prediction, extractive or generative
    config['predict_path']    = config['path_experiment'] + '/predict.' + config['timemark']+ '/'
                                # '/copynet-keyphrase-all.one2one.nocopy.extractive.predict.pkl'
    if not os.path.exists(config['predict_path']):
        os.mkdir(config['predict_path'])

    # config['path_experiment'] + '/copynet-keyphrase-all.one2one.nocopy.generate.len=8.beam=50.predict.pkl'
    # '/copynet-keyphrase-all.one2one.nocopy.extract.predict.pkl'
    #config['path_experiment'] + '/'+ config['task_name']+ '.' + config['predict_type'] + ('.len={0}.beam={1}'.format(config['max_len'], config['sample_beam'])) + '.predict.pkl' # prediction on testing data

    # Evaluation
    config['normalize_score']   = False #
    # config['normalize_score']   = True
    config['target_filter']     = 'appear-only' # whether do filtering on groundtruth? 'appear-only','non-appear-only' and None
    config['predict_filter']    = None # whether do filtering on predictions? 'appear-only'(don't work on extractive predicting),'non-appear-only' and None
    config['number_to_predict'] = 10 #the k in P@k,R@k,F1@k

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    # for w in config:
    #     print '{0} => {1}'.format(w, config[w])
    # print 'setup ok.'
    return config

def setup_keyphrase_all_testing():
    config = dict()
    # config['seed']            = 3030029828
    config['seed']            = 19900226
    # config['task_name']       = 'keyphrase-irbooks.one2one.nocopy'
    config['task_name']       = 'copynet-keyphrase-all.one2one.nocopy'
    config['timemark']        = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['clipnorm']        = 10

    config['save_updates']    = True
    config['get_instance']    = True

    config['path']            = path.realpath(path.curdir)

    config['path_experiment'] = path.realpath(path.curdir) + '/Experiment/'+config['task_name']
    config['path_h5']         = config['path_experiment']
    config['path_log']        = config['path_experiment']

    config['casestudy_log']   = config['path_experiment'] + '/case-print.log'

    config['training_name']   = 'acm-sci-journal_600k'
    config['training_dataset']= config['path'] + '/dataset/keyphrase/million-paper/all_title_abstract_keyword_clean.json'
    config['testing_name']    = 'inspec_all'
    config['testing_dataset'] = config['path'] + '/dataset/keyphrase/inspec/inspec_all.json'

    config['testing_datasets']= ['inspec']#['nus', 'semeval']
    config['preprocess_type'] = 0 # 0 is old type, 1 is new type(keep most punctuation)

    config['dataset']         = config['path'] + '/dataset/keyphrase/all_600k_dataset.pkl'
    config['voc']             = config['path'] + '/dataset/keyphrase/all_600k_voc.pkl' # for manual check

    # output log place
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])

    # trained_model
    config['trained_model']   = path.realpath(path.curdir) + '/Experiment/' + 'copynet-keyphrase-all.one2one.nocopy.<eol><digit>.emb=100.hid=150/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161129-195005.epoch=2.pkl'
    #path.realpath(path.curdir) + '/Experiment/' + 'copynet-keyphrase-all.one2one.nocopy/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161207-202026.epoch=1.batch=7200.pkl'
    # A well-trained model on all data
    #   path.realpath(path.curdir) + '/Experiment/' + 'copynet-keyphrase-all.one2one.nocopy.<eol><digit>.emb=100.hid=150/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161129-195005.epoch=2.pkl'
    # A well-trained model on acm data
    # config['path_experiment'] + '/experiments.copynet-keyphrase-all.one2one.nocopy.id=20161129-195005.epoch=2.pkl'
    config['resume_training'] = False
    config['training_archive']= config['path_experiment'] + '/save_training_status.pkl'

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 10
    config['mini_batch_size'] = 10
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = 50000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 100    # 100
    config['enc_hidden_dim']  = 150    # 150
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 100  # 100
    config['dec_hidden_dim']  = 150  # 150
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.5  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']


    # Decoder: sampling
    config['multi_output']    = False
    config['max_len']         = 8
    config['sample_beam']     = 50
    config['sample_stoch']    = False # use beamsearch
    config['sample_argmax']   = False

    config['predict_type']    = 'extractive' # type of prediction, extractive or generative
    config['predict_path']    = config['path_experiment'] + '/predict.' + config['timemark']+ '/'
                                # '/copynet-keyphrase-all.one2one.nocopy.extractive.predict.pkl'
    if not os.path.exists(config['predict_path']):
        os.mkdir(config['predict_path'])

    # config['path_experiment'] + '/copynet-keyphrase-all.one2one.nocopy.generate.len=8.beam=50.predict.pkl'
    # '/copynet-keyphrase-all.one2one.nocopy.extract.predict.pkl'
    #config['path_experiment'] + '/'+ config['task_name']+ '.' + config['predict_type'] + ('.len={0}.beam={1}'.format(config['max_len'], config['sample_beam'])) + '.predict.pkl' # prediction on testing data

    # Evaluation
    config['normalize_score']   = False #
    # config['normalize_score']   = True
    config['target_filter']     = 'appear-only' # whether do filtering on groundtruth? 'appear-only','non-appear-only' and None
    config['predict_filter']    = None # whether do filtering on predictions? 'appear-only'(don't work on extractive predicting),'non-appear-only' and None

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    # for w in config:
    #     print '{0} => {1}'.format(w, config[w])
    # print 'setup ok.'
    return config


def setup_keyphrase_acm():
    config = dict()
    # config['seed']            = 3030029828
    config['seed']            = 19900226
    config['task_name']       = 'copynet-keyphrase-acm'
    config['timemark']        = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True

    config['path']            = path.realpath(path.curdir)

    config['path_experiment'] = path.realpath(path.curdir) + '/Experiment/'+config['task_name']
    config['path_h5']         = config['path_experiment']
    config['path_log']        = config['path_experiment']

    config['training_dataset']= config['path'] + '/dataset/keyphrase/million-paper/acm_title_abstract_keyword_clean.json'
    config['testing_dataset'] = config['path'] + '/dataset/keyphrase/inspec/inspec_all.json'
    config['dataset']         = config['path'] + '/dataset/keyphrase/acm_80k_dataset.pkl'
    config['voc']             = config['path'] + '/dataset/keyphrase/acm_80k_voc.pkl'

    config['trained_model']   = config['path_experiment'] + '/experiments.copynet-keyphrase-acm.id=20161127-185055.epoch=2.batch=3000-33586.pkl'

    # output log place
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])

    # trained_model
    config['trained_model']   = None #config['path'] + '/experiments.acm_keyphrase.id='+time.strftime('%Y%m%d-%H%M%S')+'.epoch=.voc_size='+str(config['voc_size'])+'.pkl'

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 5
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = 20000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 100    # 100
    config['enc_hidden_dim']  = 150    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 100  # 100
    config['dec_hidden_dim']  = 150  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']


    # Decoder: sampling
    config['multi_output']    = False
    config['max_len']         = 10
    config['sample_beam']     = 15
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    # for w in config:
    #     print '{0} => {1}'.format(w, config[w])
    # print 'setup ok.'
    return config

def setup_keyphrase_inspec():
    config = dict()
    # config['seed']            = 3030029828
    config['seed']            = 19900226
    config['task_name']       = 'copynet-keyphrase-inspec'
    config['timemark']        = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True

    config['path']            = path.realpath(path.curdir)

    config['path_experiment'] = path.realpath(path.curdir) + '/Experiment/'+config['task_name']
    config['path_h5']         = config['path_experiment']
    config['path_log']        = config['path_experiment']

    config['training_dataset']= config['path'] + '/dataset/keyphrase/inspec/inspec_all.json'
    config['testing_dataset'] = config['path'] + '/dataset/keyphrase/inspec/inspec_all.json'
    config['dataset']         = config['path'] + '/dataset/keyphrase/inspec_5k_dataset.pkl'
    config['voc']             = config['path'] + '/dataset/keyphrase/inspec_5k_voc.pkl'

    # output log place
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])

    # trained_model
    config['trained_model']   = None #config['path'] + '/experiments.acm_keyphrase.id='+time.strftime('%Y%m%d-%H%M%S')+'.epoch=.voc_size='+str(config['voc_size'])+'.pkl'

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 20
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = -1

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 20    # 100
    config['enc_hidden_dim']  = 20    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 20  # 100
    config['dec_hidden_dim']  = 20  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']


    # Decoder: sampling
    config['multi_output']    = False
    config['max_len']         = 27
    config['sample_beam']     = 8
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    # for w in config:
        # print '{0} => {1}'.format(w, config[w])
    # print 'setup ok.'
    return config

def setup_bAbI():
    config = dict()
    # config['seed']            = 3030029828
    config['seed']            = 19920206
    config['task']            = 'bAbI'

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True
    config['path']            = path.realpath(path.pardir) + '/'
    config['path_h5']         = config['path'] + '/H5'
    config['input_dataset']   = path.realpath(path.pardir) + '/dataset/bAbI/en-10k/'
    config['dataset']         = config['path'] + '/dataset/bAbI/dataset-b.pkl'
    config['voc']             = config['path'] + '/dataset/bAbI/voc-b.pkl'

    # output log place
    config['path_log']        = config['path'] + 'Logs'
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 200
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 100    # 100
    config['enc_hidden_dim']  = 150    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 100  # 100
    config['dec_hidden_dim']  = 150  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = True
    config['identity']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']


    # Decoder: sampling
    config['max_len']         = 27
    config['sample_beam']     = 8
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    for w in config:
        print '{0} => {1}'.format(w, config[w])
    print 'setup ok.'
    return config


def setup_syn():
    config = dict()
    config['seed']            = 3030029828
    # config['seed']            = 19920206

    # model ids
    # voc_size 10000:  20160224-021106
    # voc_size 5000 :  20160224-144747 / 20160224-162424 (discard UNK)

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True
    config['path']            = path.realpath(path.curdir)
    config['path_h5']         = config['path'] + '/H5'
    # config['dataset']         = config['path'] + '/dataset/lcsts_data-word-full.pkl'
    config['dataset']         = config['path'] + '/dataset/synthetic_data_c.pkl'
    config['modelname']       = 'syn'

    # output log place
    config['path_log']        = config['path'] + '/Logs'
    config['path_logX']       = config['path'] + '/LogX'
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])
    if not os.path.exists(config['path_logX']):
        os.mkdir(config['path_logX'])

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 20
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = -1     # 20000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 150    # 100
    config['enc_hidden_dim']  = 300    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    # config['encode_max_len']  = 57
    config['decode_unk']      = False
    config['explicit_loc']    = True

    # Decoder: dimension
    config['dec_embedd_dim']  = 150  # 100
    config['dec_hidden_dim']  = 300  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']
    if config['explicit_loc']:
        config['dec_contxt_dim'] += config['encode_max_len']

    # Decoder: CopyNet
    config['copynet']         = True   # False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']

    # Decoder: sampling
    config['max_len']         = 57
    config['sample_beam']     = 10
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    for w in config:
        print '{0} => {1}'.format(w, config[w])
    print 'setup ok.'
    return config

    # config = dict()
    # # config['seed']            = 3030029828
    # config['seed']            = 19920206
    #
    # config['use_noise']       = False
    # config['optimizer']       = 'adam'
    # config['save_updates']    = True
    # config['get_instance']    = True
    # config['path']            = '/home/thoma/Work/Dial-DRL'  # path.realpath(path.curdir) + '/'
    # config['path_h5']         = config['path'] + '/H5'
    # config['dataset']         = config['path'] + '/dataset/synthetic_data_b.pkl'
    #
    # # output log place
    # config['path_log']        = config['path'] + 'Logs'
    # if not os.path.exists(config['path_log']):
    #     os.mkdir(config['path_log'])
    #
    # # # output hdf5 file.
    # # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # # if not os.path.exists(config['weights_file']):
    # #     os.mkdir(config['weights_file'])
    #
    # # size
    # config['batch_size']      = 20
    # config['mode']            = 'RNN'  # NTM
    # config['binary']          = False
    #
    # # Encoder: Model
    # config['bidirectional']   = True
    # config['enc_use_contxt']  = False
    # config['enc_learn_nrm']   = True
    # config['enc_embedd_dim']  = 150    # 100
    # config['enc_hidden_dim']  = 500    # 180
    # config['enc_contxt_dim']  = 0
    # config['encoder']         = 'RNN'
    # config['pooling']         = False
    #
    # # Decoder: dimension
    # config['dec_embedd_dim']  = 150  # 100
    # config['dec_hidden_dim']  = 500  # 180
    # config['dec_contxt_dim']  = config['enc_hidden_dim']       \
    #                             if not config['bidirectional'] \
    #                             else 2 * config['enc_hidden_dim']
    #
    # # Decoder: CopyNet
    # config['copynet']         = True   # False
    # config['identity']        = False
    # config['location_embed']  = True
    #
    # # Decoder: Model
    # config['shared_embed']    = False
    # config['use_input']       = True
    # config['bias_code']       = True
    # config['dec_use_contxt']  = True
    # config['deep_out']        = False
    # config['deep_out_activ']  = 'tanh'  # maxout2
    # config['bigram_predict']  = True
    # config['context_predict'] = True
    # config['dropout']         = 0.0  # 5
    # config['leaky_predict']   = False
    #
    # config['dec_readout_dim'] = config['dec_hidden_dim']
    # if config['dec_use_contxt']:
    #     config['dec_readout_dim'] += config['dec_contxt_dim']
    # if config['bigram_predict']:
    #     config['dec_readout_dim'] += config['dec_embedd_dim']
    #
    # # Decoder: sampling
    # config['max_len']         = 57
    # config['sample_beam']     = 8
    # config['sample_stoch']    = False
    # config['sample_argmax']   = False
    #
    # # Gradient Tracking !!!
    # config['gradient_check']  = True
    # config['gradient_noise']  = True
    #
    # config['skip_size']       = 15
    #
    # for w in config:
    #     print '{0} => {1}'.format(w, config[w])
    # print 'setup ok.'
    # return config


def setup_bst():
    config = dict()
    config['seed']            = 3030029828
    # config['seed']            = 19920206

    # model ids
    # voc_size 10000:  20160224-021106
    # voc_size 5000 :  20160224-144747 / 20160224-162424 (discard UNK)

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True
    config['path']            = path.realpath(path.curdir)
    config['path_h5']         = config['path'] + '/H5'
    # config['dataset']         = config['path'] + '/dataset/lcsts_data-word-full.pkl'
    config['dataset']         = config['path'] + '/dataset/BST_1M.data.pkl'
    config['modelname']       = 'bst'

    # output log place
    config['path_log']        = config['path'] + '/Logs'
    config['path_logX']       = config['path'] + '/LogX'
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])
    if not os.path.exists(config['path_logX']):
        os.mkdir(config['path_logX'])

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 20
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = -1     # 20000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 150    # 100
    config['enc_hidden_dim']  = 300    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    config['decode_unk']      = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 150  # 100
    config['dec_hidden_dim']  = 300  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = False  # True   # False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False
    config['encourage_gen']   = 0.1    # lambda if 0 no encourage

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']

    # Decoder: sampling
    config['max_len']         = 100
    config['sample_beam']     = 10
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    for w in config:
        print '{0} => {1}'.format(w, config[w])
    print 'setup ok.'
    return config


def setup_lcsts():
    config = dict()
    config['seed']            = 3030029828
    # config['seed']            = 19920206

    # model ids
    # voc_size 10000:  20160224-021106
    # voc_size 5000 :  20160224-144747 / 20160224-162424 (discard UNK)

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True
    config['path']            = path.realpath(path.curdir)
    config['path_h5']         = config['path'] + '/H5'
    config['dataset']         = config['path'] + '/dataset/lcsts_data-word-full.pkl'
    # config['dataset']         = config['path'] + '/dataset/lcsts_data-word.pkl'
    config['modelname']       = 'LCSTS'
    config['segment']         = True

    # output log place
    config['path_log']        = config['path'] + '/Logs'
    config['path_logX']       = config['path'] + '/LogX'
    config['path_model']      = config['path'] + '/H5'
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])
    if not os.path.exists(config['path_logX']):
        os.mkdir(config['path_logX'])

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 20
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = 20000   # 20000

    # # based on characters (modified)
    # config['segment']         = False
    # config['dataset']         = config['path'] + '/dataset/lcsts_data-char-full.pkl'
    # config['modelname']       = 'LCSTS-CCC'
    # config['voc_size']        = 3000

    # trained_model
    # config['trained_model']   = config['path_model'] + '/experiments.CopyLCSTSXXX.id=20160305-004957.epoch=1.iter=20000.pkl'
    # config['trained_model']   = config['path_model'] + '/experiments.CopyLCSTSXXX.id=20160301-105813.epoch=2.iter=80000.pkl'
    config['trained_model']   = config['path_model'] + '/experiments.CopyLCSTSXXX.id=20160301-114653.epoch=2.iter=100000.pkl'

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 500    # 100
    config['enc_hidden_dim']  = 750    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    config['encode_max_len']  = 140
    config['decode_unk']      = False

    # Decoder: sample
    config['max_len']         = 33
    config['sample_beam']     = 30  # 10
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Decoder: train
    config['dec_embedd_dim']  = 500  # 100
    config['dec_hidden_dim']  = 750  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    config['explicit_loc']    = False
    if config['explicit_loc']:
        config['dec_contxt_dim'] += config['encode_max_len']

    # Decoder: CopyNet
    config['copynet']         = True   # False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    for w in config:
        print '{0} => {1}'.format(w, config[w])
    print 'setup ok.'
    return config


def setup_weibo():
    config = dict()
    config['seed']            = 3030029828
    # config['seed']            = 19920206

    # model ids

    config['use_noise']       = False
    config['optimizer']       = 'adam'
    config['save_updates']    = True
    config['get_instance']    = True
    config['path']            = path.realpath(path.curdir)
    config['path_h5']         = config['path'] + '/H5'
    # config['dataset']         = config['path'] + '/dataset/lcsts_data-word-full.pkl'
    # config['dataset']         = config['path'] + '/dataset/weibo_data-word-cooc.pkl'
    config['dataset']         = config['path'] + '/dataset/movie_dialogue_data.pkl'

    # output log place
    config['path_log']        = config['path'] + '/Logs'
    config['path_logX']       = config['path'] + '/LogX'
    if not os.path.exists(config['path_log']):
        os.mkdir(config['path_log'])
    if not os.path.exists(config['path_logX']):
        os.mkdir(config['path_logX'])

    # # output hdf5 file.
    # config['weights_file']    = config['path'] + '/froslass/model-pool/'
    # if not os.path.exists(config['weights_file']):
    #     os.mkdir(config['weights_file'])

    # size
    config['batch_size']      = 20
    config['mode']            = 'RNN'  # NTM
    config['binary']          = False
    config['voc_size']        = 10000  # 30000

    # Encoder: Model
    config['bidirectional']   = True
    config['enc_use_contxt']  = False
    config['enc_learn_nrm']   = True
    config['enc_embedd_dim']  = 350    # 100
    config['enc_hidden_dim']  = 500    # 180
    config['enc_contxt_dim']  = 0
    config['encoder']         = 'RNN'
    config['pooling']         = False

    config['decode_unk']      = False
    config['utf-8']           = False

    # Decoder: dimension
    config['dec_embedd_dim']  = 350  # 100
    config['dec_hidden_dim']  = 500  # 180
    config['dec_contxt_dim']  = config['enc_hidden_dim']       \
                                if not config['bidirectional'] \
                                else 2 * config['enc_hidden_dim']

    # Decoder: CopyNet
    config['copynet']         = True # False   # False
    config['identity']        = False
    config['location_embed']  = True
    config['coverage']        = True
    config['copygate']        = True
    config['killcopy']        = False

    # Decoder: Model
    config['shared_embed']    = False
    config['use_input']       = True
    config['bias_code']       = True
    config['dec_use_contxt']  = True
    config['deep_out']        = False
    config['deep_out_activ']  = 'tanh'  # maxout2
    config['bigram_predict']  = True
    config['context_predict'] = True
    config['dropout']         = 0.0  # 5
    config['leaky_predict']   = False

    config['dec_readout_dim'] = config['dec_hidden_dim']
    if config['dec_use_contxt']:
        config['dec_readout_dim'] += config['dec_contxt_dim']
    if config['bigram_predict']:
        config['dec_readout_dim'] += config['dec_embedd_dim']

    # Decoder: sampling
    config['max_len']         = 50
    config['sample_beam']     = 10
    config['sample_stoch']    = False
    config['sample_argmax']   = False

    # Gradient Tracking !!!
    config['gradient_check']  = True
    config['gradient_noise']  = True

    config['skip_size']       = 15

    conc = sorted(config.items(), key=lambda c:c[0])
    for c, v in conc:
        print '{0} => {1}'.format(c, v)
    print 'setup ok.'
    return config
