package model

type Noun struct {
	Name string `json:"name" sql:"not null" valid:"required"`
}
