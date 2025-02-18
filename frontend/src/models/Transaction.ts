export class Transaction {
    _id: number
    _user: string
    _type: string
    _category: string
    _amount: number
    _description: string
    _date: string
    _time: string

    constructor(id: number, user: string, type: string, category: string, amount: number, description: string, date: string, time: string) {
        this._id = id
        this._user = user
        this._type = type
        this._category = category
        this._amount = amount
        this._description = description
        this._date = date
        this._time = time
    }

    get id() {
        return this._id
    }

    get user() {
        return this._user
    }

    get type() {
        return this._type.toLowerCase()
    }

    get category() {
        return this._category.toLowerCase()
    }

    get amount() {
        return Number(this._amount)
    }

    get description() {
        return this._description
    }

    set description(value: string) {
        this._description = value
    }

    get date() {
        return new Date(this._date)
    }

    get time() {
        return this._time
    }
}
