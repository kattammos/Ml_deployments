import sys

sys.append("C:\\Users\\User\\OneDrive\\Документы\\KV_DW_JL_5\\Ml_deployments\\production_model_package")

from regression_model.config.core import config
from regression_model.processing.features import TemporalVariableTransformer


def test_temporal_variable_transformer(sample_input_data):

    #Given
    transformer = TemporalVariableTransformer(
        variable=config.model_config.temporal_vars,
        reference_variable=config.model_config.ref_var
    )


    assert sample_input_data["YearRemodAdd"].iat[0] == 1961


    #When
    subject = transformer.fit_transform(sample_input_data)

    #Then
    assert subject["YearRemodAdd"].iat[0] == 49
    