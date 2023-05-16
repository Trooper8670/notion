import graphene
from graphql.execution.base import ResolveInfo
from graphql_auth.bases import Output
from graphene_file_upload.scalars import Upload
from image_cropping import ImageRatioField

from .forms import CreateCropImageMutationForm


class CreateCropImageMutation(graphene.Mutation, Output):
    form = CreateCropImageMutationForm

    class Arguments:
        """Necessary input to create a new Company."""
        name = graphene.String(required=True, description="Company name")
        logo = Upload(required=False, description="Logo for the Company.")

    @staticmethod
    def mutate(self, info: ResolveInfo, logo=None, **data) -> "CreateCropImageMutation":
        """Mutate method."""
        file_data = {}
        if logo:
            file_data = {"logo": logo}

        # https://docs.djangoproject.com/en/3.2/ref/forms/api/#binding-uploaded-files-to-a-form
        # Binding file data to the Form.
        f = CreateCropImageMutation.form(data, file_data)

        if f.is_valid():
            f.save()
            return CreateCropImageMutation(success=True)
        else:
            return CreateCropImageMutation(
                success=False, errors=f.errors.get_json_data()
            )