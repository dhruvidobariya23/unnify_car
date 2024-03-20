# Register your models here.
import core.models as core_models
from django.contrib import admin

admin.site.register(core_models.AuthTokens)

class CheckoutsAdmin(admin.ModelAdmin):
    list_display=['owner_name','email','company_name','mobile']
admin.site.register(core_models.Checkouts,CheckoutsAdmin)

class FinancierAdmin(admin.ModelAdmin):
    list_display=['financier_name','financier_type','financier_code']
admin.site.register(core_models.Financier,FinancierAdmin)

class FlowDetailsAdmin(admin.ModelAdmin):
    list_display=['name','email','make_name','model_name','variant_name']
admin.site.register(core_models.FlowDetails,FlowDetailsAdmin)

class GetInTouchesAdmin(admin.ModelAdmin):
    list_display=['contact','is_connected','remark']
admin.site.register(core_models.GetInTouches,GetInTouchesAdmin)

class GodigitVehicalMastersAdmin(admin.ModelAdmin):
    list_display=['vehicle_code','make_name','model_name','variant_name','vehicle_type']
admin.site.register(core_models.GodigitVehicalMasters,GodigitVehicalMastersAdmin)

class InsuranceCompaniesAdmin(admin.ModelAdmin):
    list_display=['name','logo']
admin.site.register(core_models.InsuranceCompanies,InsuranceCompaniesAdmin)

class MainMasterAdmin(admin.ModelAdmin):
    list_display=['vehicle_code','make','model','variant','cc','fule_type']
admin.site.register(core_models.MainMaster,MainMasterAdmin)

class MakesAdmin(admin.ModelAdmin):
    list_display=['make_name']
admin.site.register(core_models.Makes,MakesAdmin)

class ModelsAdmin(admin.ModelAdmin):
    list_display=['model_name','make']
admin.site.register(core_models.Models,ModelsAdmin)

class PincodeMastersAdmin(admin.ModelAdmin):
    list_display=['pincode','office_name']
admin.site.register(core_models.PincodeMasters,PincodeMastersAdmin)

class PreviousInsurerMastersAdmin(admin.ModelAdmin):
    list_display=['company_code','insurer_name','source','insurer_master']
admin.site.register(core_models.PreviousInsurerMasters,PreviousInsurerMastersAdmin)

class ProposalsAdmin(admin.ModelAdmin):
    list_display=['quote','insurance_company','email','proposal_responses']
admin.site.register(core_models.Proposals,ProposalsAdmin)

class QuoteResponseDataAdmin(admin.ModelAdmin):
    list_display=['quoteid','quoteresponseid','response']
admin.site.register(core_models.QuoteResponseData,QuoteResponseDataAdmin)

class QuoteResponsesAdmin(admin.ModelAdmin):
    list_display=['insurer_name','quote_id']
admin.site.register(core_models.QuoteResponses,QuoteResponsesAdmin)

class QuotesAdmin(admin.ModelAdmin):
    list_display=['flow','policy_type','cover_idv','previous_policy_type']
admin.site.register(core_models.Quotes,QuotesAdmin)

class RtoMastersAdmin(admin.ModelAdmin):
    list_display=['rto_name','rto_code','city','pincode']
admin.site.register(core_models.RtoMasters,RtoMastersAdmin)

class TransactionsAdmin(admin.ModelAdmin):
    list_display=['policypdfresponse','kycresponse','insurername']
admin.site.register(core_models.Transactions,TransactionsAdmin)

class VariantsAdmin(admin.ModelAdmin):
    list_display=['variant_name','fuel_type','model','vehicle_code']
admin.site.register(core_models.Variants,VariantsAdmin)

class VehicalMastersAdmin(admin.ModelAdmin):
    list_display=['vehical_code','vehical_make','vehical_model','vehical_variant','fuel_type']
admin.site.register(core_models.VehicalMasters,VehicalMastersAdmin)

class ZoopMastersAdmin(admin.ModelAdmin):
    list_display=['car_no','details']
admin.site.register(core_models.ZoopMasters,ZoopMastersAdmin)