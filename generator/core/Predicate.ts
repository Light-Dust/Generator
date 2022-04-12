class Predicate {
    private file: string = null;
    private condition: PredicateCondition = null;
    private terms: Predicate = null;
    private block: MCBlock = null;
    private properties: string = null;
    private predicate: string = null;
    private entity: "this" | "killer" | "killer_player" = null;
    private scores: { [key: string]: number } | { [key: string]: { 'min': number, 'max': number } } = null;
    private inverse: boolean = null;
    private offsetX: number = 0;
    private offsetY: number = 0;
    private offsetZ: number = 0;
    private chance: number = 0;
    private looting_multiplier: number = 0;
    private name: Predicate = null;
    private enchantment: MCEnchantment = null;
    private chances: { [key: number]: number } = null;
    private value: number | { 'min': number, 'max': number } = 0;
    private raining: boolean = null;
    private thundering: boolean = null;
    private range: number | { 'min': number, 'max': number } = 0;

    constructor(file: string,condition: PredicateCondition, terms?: Predicate, block?: MCBlock, properties?: string, predicate?: string, entity?: "this" | "killer" | "killer_player", scores?: { [key: string]: number } | { [key: string]: { 'min': number, 'max': number } }, inverse?: boolean, offsetX?: number, offsetY?: number, offsetZ?: number, chance?: number, looting_multiplier?: number, name?: Predicate, enchantment?: MCEnchantment, chances?: { [key: number]: number }, value?: number | { 'min': number, 'max': number }, raining?: boolean, thundering?: boolean, range?: number | { 'min': number, 'max': number }) {
        this.file = file;
        this.condition = condition;
        this.terms = terms;
        this.block = block;
        this.properties = properties;
        this.predicate = predicate;
        this.entity = entity;
        this.scores = scores;
        this.inverse = inverse;
        this.offsetX = offsetX;
        this.offsetY = offsetY;
        this.offsetZ = offsetZ;
        this.chance = chance;
        this.looting_multiplier = looting_multiplier;
        this.name = name;
        this.enchantment = enchantment;
        this.chances = chances;
        this.value = value;
        this.raining = raining;
        this.thundering = thundering;
        this.range = range;
    }

    public getJson(): string {
        /**
         * @returns 返回当前战利品表谓词的JSON文本
         */
        let json: any = {};
        if (this.condition) {
            json['condition'] = this.condition;
        }
        if (this.terms) {
            json['terms'] = this.terms.getJson();
        }
        if (this.block) {
            json['block'] = this.block;
        }
        if (this.properties) {
            json['properties'] = this.properties;
        }
        if (this.predicate) {
            json['predicate'] = this.predicate;
        }
        if (this.entity) {
            json['entity'] = this.entity;
        }
        if (this.scores) {
            json['scores'] = this.scores;
        }
        if (this.inverse) {
            json['inverse'] = this.inverse;
        }
        if (this.offsetX) {
            json['offsetX'] = this.offsetX;
        }
        if (this.offsetY) {
            json['offsetY'] = this.offsetY;
        }
        if (this.offsetZ) {
            json['offsetZ'] = this.offsetZ;
        }
        if (this.chance) {
            json['chance'] = this.chance;
        }
        if (this.looting_multiplier) {
            json['looting_multiplier'] = this.looting_multiplier;
        }
        if (this.name) {
            json['name'] = this.name.file;
        }
        if (this.enchantment) {
            json['enchantment'] = this.enchantment;
        }
        if (this.chances) {
            json['chances'] = this.chances;
        }
        if (this.value) {
            json['value'] = this.value;
        }
        if (this.raining) {
            json['raining'] = this.raining;
        }
        if (this.thundering) {
            json['thundering'] = this.thundering;
        }
        if (this.range) {
            json['range'] = this.range;
        }
        return json.toString();
    }
}

enum PredicateCondition {
    ALTERNATIVE = 'minecraft:alternative',
    BLOCK_STATE_PROPERTY = 'minecraft:block_state_property',
    DAMAGE_SOURCE_PROPERTIES = 'minecraft:damage_source_properties',
    ENTITY_PROPERTIES = 'minecraft:entity_properties',
    ENTITY_SCORES = 'minecraft:entity_scores',
    INVERTED = 'minecraft:inverted',
    KILLED_BY_PLAYER = 'minecraft:killed_by_player',
    LOCATION_CHECK = 'minecraft:location_check',
    MATCH_TOOL = 'minecraft:match_tool',
    RANDOM_CHANCE = 'minecraft:random_chance',
    RANDOM_CHANCE_WITH_LOOTING = 'minecraft:random_chance_with_looting',
    REFERENCE = 'minecraft:reference',
    SURVIVES_EXPLOSION = 'minecraft:survives_explosion',
    TABLE_BONUS = 'minecraft:table_bonus',
    TIME_CHECK = 'minecraft:time_check',
    WATHER_CHECK = 'minecraft:wather_check',
    VALUE_CHECK = 'minecraft:value_check'
}

console.log(new Predicate('test',PredicateCondition.ALTERNATIVE).getJson());
