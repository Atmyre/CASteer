"""
Prompt pair construction for computing CASteer steering vectors.

Each function returns (positive_prompts, negative_prompts) where the only
difference between a positive and its corresponding negative prompt is the
presence of the target concept.
"""


def get_imagenet_classes(num=50):
    imagenet_classes = []
    f = open('imagenet_classes.txt', 'r')
    for line in f.readlines():
        imagenet_classes.append(line.strip())
    f.close()
    return imagenet_classes


def get_prompts_concrete(num=50, concept_pos='Snoopy', concept_neg=None):
    """
    Paired prompts for concrete concepts (objects, characters).

    Positive: "{ImageNet class} with {concept}"
    Negative: "{ImageNet class}" (or with concept_neg if specified)
    """
    imagenet_classes = get_imagenet_classes(num)

    prompts_pos = []
    prompts_neg = []
    for cls in imagenet_classes[:num]:
        prompts_pos.append(cls + ' with {}'.format(concept_pos))
        if concept_neg is not None:
            prompts_neg.append(cls + ' with {}'.format(concept_neg))
        else:
            prompts_neg.append(cls)

    return prompts_pos, prompts_neg


def get_prompts_style(num=50, concept_pos='anime', concept_neg=None):
    """
    Paired prompts for style concepts (artistic styles).

    Positive: "{ImageNet class}, {style} style"
    Negative: "{ImageNet class}" (or with concept_neg style if specified)
    """
    imagenet_classes = get_imagenet_classes(num)

    prompts_pos = []
    prompts_neg = []
    for cls in imagenet_classes[:num]:
        prompts_pos.append(cls + ', {} style'.format(concept_pos))
        if concept_neg is not None:
            prompts_neg.append(cls + ', {} style'.format(concept_neg))
        else:
            prompts_neg.append(cls)

    return prompts_pos, prompts_neg


def get_prompts_human_related(concept_pos='nudity', concept_neg=None):
    """
    Paired prompts for human-related / abstract concepts (safety, NSFW).

    Positive: "{person} {scene}, {concept}"
    Negative: "{person} {scene}" (or with concept_neg if specified)

    Generates 8 x 13 = 104 prompt pairs.
    """
    B = ['a girl', 'a boy', 'two men', 'two women', 'two people', 'a man', 'a woman', 'an old man', 'an old woman', 'boys', 'girls', 'men', 'women', 'group of people', 'a human']
    C = ['', 'gloomy image', 'zoomed in', 'talking', 'on the street', 'in a strange pose', 'realism', \
         'colorful background', 'on a beach', 'playing guitar', 'enjoying nature', 'smiling', 'in a futuristic spaceship', 'with kittens']

    prompts_pos = []
    prompts_neg = []
    for b in B:
        for c in C:
            prompts_pos.append(b + ' ' + c + ', {}'.format(concept_pos))
            if concept_neg is not None:
                prompts_neg.append(b + ' ' + c + ', {}'.format(concept_neg))
            else:
                prompts_neg.append(b + ' ' + c)

    return prompts_pos, prompts_neg
