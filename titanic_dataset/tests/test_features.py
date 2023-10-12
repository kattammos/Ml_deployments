import sys

sys.path.append("C:\\Users\\User\\OneDrive\\Документы\\KV_DW_JL_5\\Ml_deployments\\titanic_dataset\\")

from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer

def test_temporal_variable_transformer(sample_input_data):

    #Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.cabin_vars
    )

    assert sample_input_data['cabin'].iat[6] == 'E12'

    
    #When
    subject = transformer.fit_transform(sample_input_data)

    #Then
    assert subject['cabin'].iat[6] == 'E'