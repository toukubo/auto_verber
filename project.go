package model

type Project struct {
	BaseModel
	Name        string `json:"name" sql:"not null" valid:"required"`
	Type        string `json:"type" sql:"not null" valid:"required"`
	LambdaId    string `json:"lambda_id"`
	Description string `json:"description" sql:"not null" valid:"required"`
	OwnerId     string `json:"owner_id" sql:"not null" valid:"required"`
	BaseImageId string `json:"base_image_id" sql: "not null" valid:"required"`
}
